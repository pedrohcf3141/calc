from sqlalchemy import ForeignKey
from datetime import datetime
from edukalculadora.db import db
from edukalculadora import app
import math

class Operacao(db.Model):
    __tablename__ = "operacoes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(8), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Operacao %r>" % self.id
    
    def __str__(self):
        return self.nome

# class TipoEquacao(db.Model):
#     pass



class Mudanca(db.Model):
    __tablename__ = "mudancas"

    id = db.Column(db.Integer, primary_key=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    modificado_em = db.Column(db.DateTime, default=datetime.utcnow)
    cotg = db.Column(db.String(64), nullable=True)
    valor1 = db.Column(db.Float, nullable=False)
    valor2 = db.Column(db.Float, nullable=True)
    resposta = db.Column(db.String(64), nullable=True)
    equacao = db.Column(db.Integer, ForeignKey("equacoes.id", ondelete="CASCADE"), nullable=True)
    operacao = db.Column(db.Integer, ForeignKey("operacoes.id", ondelete="CASCADE"))

    @property
    def soma(self):
        return f'{(self.valor1 + self.valor2):.2f}'

    @property
    def subtracao(self):
        return f'{(self.valor1 - self.valor2):.2f}'
    
    @property
    def multiplicacao(self):
        return self.valor1 * self.valor2
    
    @property
    def divisao(self):
        return f'{(self.valor1 / self.valor2):.2f}'

    @property
    def calculo(self):     
        dicionario_operacoes = {
            1:self.soma,
            2:self.subtracao,
            4:self.multiplicacao,
            3:self.divisao
        }
        if self.operacao in dicionario_operacoes:
            self.resposta = dicionario_operacoes[self.operacao]
        return self.resposta

    def cotangente(self):
        try:
            self.cotg = f'{(1/math.tan(float(self.resposta))):.2f}'
        except:
            self.cotg = '' 
        self.modificado_em = datetime.now()


class Equacao(db.Model):
    
    __tablename__ = "equacoes"

    id = db.Column(db.Integer, primary_key=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    mudancas = db.relationship("Mudanca", backref="mudancas", passive_deletes=True, passive_updates=True)

    def get_id(self):
        return int(self.id)

    def __repr__(self):
        return "<Equacao %r>" % self.id

