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

class Equacao(db.Model):
    
    __tablename__ = "equacoes"

    id = db.Column(db.Integer, primary_key=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    modificado_em = db.Column(db.DateTime, default=datetime.utcnow)
    valor1 = db.Column(db.Float, nullable=False)
    valor2 = db.Column(db.Float, nullable=True)
    operacao = db.Column(db.Integer, ForeignKey("operacoes.id", ondelete="CASCADE"))

    def __repr__(self):
        return "<Equacao %r>" % self.id

    @property
    def soma(self):
        return f'{(self.valor1 + (self.valor2 or 0)):.2f}'

    @property
    def subtracao(self):
        return f'{(self.valor1 - (self.valor2 or 0)):.2f}'
    
    @property
    def multiplicacao(self):
        return self.valor1 * (self.valor2 or 1)
    
    @property
    def divisao(self):
        return f'{(self.valor1 / (self.valor2 or 1)):.2f}'

    @property
    def cotg(self):
        return f'{(1/math.tan(self.valor1)):.2f}' 

    @property
    def resposta(self):
        dicionario_operacoes = {
            1:self.soma,
            2:self.subtracao,
            4:self.multiplicacao,
            3:self.divisao,
            5:self.cotg,
        }
        if self.operacao in dicionario_operacoes:
            return dicionario_operacoes[self.operacao]
        return 0
