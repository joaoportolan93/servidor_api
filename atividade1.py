from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request 
# Inicializando o banco de dados
db = SQLAlchemy()

# Definindo o modelo para o Lead
class Lead(db.Model):
    __tablename__ = 'leads'
    
    def create_lead(self, name, email, telefone):
        lead = Lead(name=name, email=email, telefone=telefone )
        self.db.session.add(lead)
        self.db.session.commit()
        def __init__(self, name, email, telefone ):
            self.name = name
        self.email = email
        self.telefone = telefone
     

    # Função para retornar os dados como dicionário
        def as_dict(self):
            return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'telefone' : self.telefone
        }
