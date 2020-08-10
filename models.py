from sqlalchemy import create_engine, Column, Integer,String,ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///produtos.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#Criação de tabelas:
class Produtos(Base):
    __tablename__='produtos' #nome atribuido a tabela.
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), index=True)
    codigo = Column(String(40))
    valor = (Integer)
    quantidade = (Integer)

    def __repr__(self):
        return '<Produto {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()