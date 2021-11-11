from flask_wtf  import  FlaskForm
from wtforms  import (
    StringField, PasswordField,
    TextAreaField, SubmitField,
    IntegerField, SelectField, 
    FieldList, FormField,
    Form, HiddenField, FloatField
)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import(
    InputRequired, Length,
    AnyOf, DataRequired, NumberRange
)
from edukalculadora.models.tables import (
    Operacao, Equacao, Mudanca
)
from edukalculadora import app


class OperacaoForm(FlaskForm):

    nome = StringField(
        'Operacao',
        validators=[
            DataRequired(message='Uma Operação é exigida'),
            Length(min=1, max=64, message= 'opções são soma, subtração, divisão, multiplicação e cotangente')
            ]
        )
    submit = SubmitField('Adicinar')


class MudancaForm(FlaskForm):
    valor1 = FloatField(
        'Primeiro Valor',
        validators=[
            DataRequired(message='Uma Instrução é exigida'),
            ]
        )
    operacao = QuerySelectField(
        "Operação",
        query_factory=Operacao.query.all,
        get_pk=lambda u: u.id,
        get_label=lambda u: u.nome
    )
    valor2 = FloatField(
        'Segundo Valor',
        validators=[
            DataRequired(message='Uma Instrução é exigida'),
            ]
        )
    submit = SubmitField('Adicinar')


class EquacaoForm(FlaskForm):
    mudanca = FieldList(FormField(MudancaForm), min_entries=1)
