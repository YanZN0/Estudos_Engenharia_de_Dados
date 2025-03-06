from sqlalchemy import create_engine


# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker, Session

Session = sessionmaker(bind=engine)
session = Session()

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    # O commit é feito automaticamente aqui, se não houver exceções
    # O rollback é automaticamente chamado se uma exceção ocorrer
    # A sessão é fechada automaticamente ao sair do bloco with
