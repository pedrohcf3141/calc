import math
from flask import Flask, render_template, request
from flask.helpers import flash

app = Flask(__name__)
import os
   
from controllers import urls
from models import tables


# @app.route("/")
# def index():
#     return render_template("index.html") 

# @app.route("/edu-kalculadora", methods=['GET', 'POST'])
# def edu-kalculadora():
#     resp = ''
#     if request.method == 'POST' and 'nro1' in request.form and 'operacao' in request.form and 'nro2' in request.form:
#         nro1 = request.form.get('nro1')
#         operacao = request.form.get('operacao')
#         nro2 = request.form.get('nro2')
#         try:
#             n1 = float(nro1)
#             n2 = float(nro2)
#         except TypeError:
#             resp = 'Valores digitados são incompativeis'
#         dic_operacoes ={
#             '+': n1 + n2,
#             '*': n1 * n2,
#             '-': n1 - n2,
#             '/': n1 / n2,
#         }
#         if operacao in dic_operacoes:
#             resp = dic_operacoes[operacao]
#         else:
#             resp = 'Operação Invalida'
#     return render_template('edu-kalculadora.html', resp=resp)


# @app.route("/cotangente", methods=['GET', 'POST'])
# def cotangente():
#     resp = ''
#     if request.method == 'POST' and 'angulo' in request.form:
#         try:
#             angulo = float(request.form.get('angulo'))
#             sen = math.sin(math.radians(float(angulo)))
#             cos = math.cos(math.radians(float(angulo)))
#             cotangente = cos / sen
#             resp = round(cotangente, 2)
#         except TypeError:
#             resp = 'Valor digitado é incompativel'
        
#     return render_template('cotangente.html', resp=resp)
 
if __name__ == "__main__":
    app.run()
