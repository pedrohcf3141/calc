from typing import Dict
from edukalculadora.db import db
from flask import (
    Flask, render_template,
    url_for, request, flash,
    redirect, session
    )
from edukalculadora.models.tables import (
    Operacao, Equacao, Mudanca
)
from .forms import(
    OperacaoForm,
    EquacaoForm,
    MudancaForm,
)
from edukalculadora import app
from datetime import timedelta

@app.route("/")
def index():
    equacoes = Equacao.query.all()
    return render_template("index.html", equacoes=equacoes) 
    

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
    form = MudancaForm()
    if form.validate_on_submit():     
        equacao = Equacao()
        db.session.add(equacao)
        db.session.commit()
        mudanca = Mudanca(
            valor1=form.valor1.data,
            valor2=form.valor2.data,
            operacao = form.operacao.data.id,
            equacao = equacao.id, 
        )
        mudanca.calculo
        db.session.add(mudanca)
        db.session.commit()
        flash('Equacao Criada com Sucesso')
        return redirect(url_for('index'))
    return render_template ('nova_equacao.html', titulo="Nova Equacao", form=form)

@app.route("/equacoes/<int:id>/mudancas/", methods=['POST', 'GET'])
def mudancas_equacao(id):
    operacoes = Operacao.query.all()
    equacao = Equacao.query.get_or_404(id)
    form = EquacaoForm()
    equacao_mudancas_qs = Mudanca.query.filter_by(equacao=id)
    if form.mudanca.data and form.mudanca.data[0]['submit'] == True:
        for mudanca in form.mudanca.data:
            mudanca = Mudanca(
            valor1=mudanca['valor1'],
            valor2=mudanca['valor2'],
            operacao = mudanca['operacao'].id,
            equacao = id, 
            )
            mudanca.calculo
            db.session.add(mudanca)
            db.session.commit()
            flash('Mudanca Criada com Sucesso')        
            # return render_template(
            #     'mudancas_equacoes.html',
            #     id=equacao.id,
            #     titulo=f"Equação {equacao.id}",
            #     form=form,
            #     equacao_mudancas_qs=equacao_mudancas_qs,
            #     operacoes=operacoes,
            # )   
        return redirect(f"/equacoes/{mudanca.equacao}/mudancas/")

    equacao_mudancas_qs = Mudanca.query.filter_by(equacao=id)
    return render_template(
        'mudancas_equacoes.html',
        id=equacao.id,
        titulo=f"LOGS da Equação {equacao.id}",
        form=form,
        equacao_mudancas_qs=equacao_mudancas_qs,
        operacoes=operacoes,
    )   

@app.route("/equacoes/<int:id>/delete_equacao/", methods=['POST', 'GET'])
def delete_equacao(id):
    mudanca = Mudanca.query.get(id)
    db.session.delete(mudanca)
    db.session.commit()
    flash('', 'success')
    return redirect(f"/equacoes/{mudanca.equacao}/mudancas/")

@app.route("/equacoes/<int:id>/cotg/", methods=['POST', 'GET'])
def cotangente(id):
    mudanca = Mudanca.query.get(id)
    mudanca.cotangente()
    db.session.add(mudanca)
    db.session.commit()
    flash('', 'success')
    return redirect(f"/equacoes/{mudanca.equacao}/mudancas/")
