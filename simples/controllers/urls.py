from typing import Dict
from edu-kalculadora.db import db
from flask import (
    Flask, render_template,
    url_for, request, flash,
    redirect, session
    )
from edu-kalculadora.models.tables import (
    Operacao, Equacao
)
from .forms import(
    OperacaoForm,
    EquacaoForm
)
from edu-kalculadora import app
from datetime import timedelta

@app.route("/")
def index():
    operacoes = Operacao.query.all()
    equacoes = Equacao.query.all()
    return render_template("index.html", equacoes=equacoes, operacoes=operacoes) 
    

@app.route('/operacoes')
def operacoes():
    operacoes = Operacao.query.all()
    return render_template ('operacoes.html', titulo="Operações Disponiveis", operacoes=operacoes)

@app.route('/nova_operacao', methods=['POST', 'GET'])
def nova_operacao():
    form = OperacaoForm()
    if form.validate_on_submit():
        operacao = Operacao(nome=form.nome.data)
        db.session.add(operacao)
        db.session.commit()
        flash('')
        return redirect(url_for('operacoes'))
    operacoes_qs = Operacao.query.all()
    return render_template ('nova_operacao.html', titulo="Nova Operacao", form=form)

@app.route('/operacoes/<id>', methods=['POST', 'GET'])
def change_operacao(id):
    operacao = Operacao.query.get_or_404(id)
    nome = operacao.nome
    form = OperacaoForm()
    if form.validate_on_submit():
        print(form.errors)
        operacao.nome=form.nome.data
        db.session.commit()
        flash('Atualizado', 'success')
        return redirect(url_for("operacoes", form=form))
    elif request.method == 'GET':
        operacao.nome = form.nome
        
    return render_template('change_operacao.html', titulo="Altere sua operacao", operacao=operacao, form=form)

@app.route('/operacoes/delete/<id>', methods=['POST', 'GET'])
def delete_operacao(id):
    operacao = Operacao.query.get_or_404(id)
    db.session.delete(operacao)
    db.session.commit()
    flash('deletado com Sucesso', 'success')
    return redirect(url_for("operacoes"))

@app.route("/equacoes", methods=["GET"])
def equacoes():
    return redirect("/")

@app.route("/nova_equacao", methods=['POST', 'GET'])
def nova_equacao():
    form = EquacaoForm()
    if form.validate_on_submit():
        equacao = Equacao(
            valor1=form.valor1.data,
            valor2=form.valor2.data,
            operacao = form.operacao.data.id
        )
        db.session.add(equacao)
        db.session.commit()
        flash('Equacao Criada com Sucesso')
        return redirect(url_for('index'))
    return render_template ('nova_equacao.html', titulo="Nova Equacao", form=form)


# @app.route("/equacoes/<int:id>", methods=['POST', 'GET'])
# def change_equacoes(id):
#     equacao = Equacao.query.get_or_404(id)
#     form = EquacaoOperacaoValorForm()
#     # if form.validate_on_submit():
#     if form.operacao.data and form.operacao.data[0]['submit'] == True:
#         for indice in form.operacao.data:
#             operacao = EquacaoOperacao(
#                 operacao=indice['equacao'],
#                 equacao_id=id
#             )
#             db.session.add(operacao)
#             db.session.commit()
#             return redirect(url_for('change_equacoes', id=equacao.id))

#     if form.valor.data and form.valor.data[0]['submit']== True:
#         for indice in form.valor.data:
#             valor = EquacaoValor(
#                 valor=indice['valor'],
#                 equacao_id=id,
#             )
#             db.session.add(valor)
#             db.session.commit()
#             return redirect(url_for('change_equacoes', id=equacao.id))
#     operacoes_qs = EquacaoOperacao.query.filter_by(equacao_id=id)
#     valores_qs = EquacaoValor.query.filter_by(equacao_id=id)
#     return render_template('equacoes.html', titulo="Equações", equacao=equacao, form=form, operacoes_qs=operacoes_qs, valores_qs=valores_qs)

