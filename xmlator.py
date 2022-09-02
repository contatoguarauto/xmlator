from sqlalchemy_firebird import fdb
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('firebird+fdb://sysdba:masterkey@localhost:3050/c:/engematica/dados/guarauto_junior.fdb')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Saidas(Base):
    __tablename__ = 'SAIDAS'

    IDSAIDA = Column(Integer, primary_key = True)
    NR_NF = Column(Integer)
    XML_NFE = Column(String)

arqAntecipacao = open('./nfsfiscais.txt')

for linha in arqAntecipacao.readlines():
    stmt = select(Saidas).where(Saidas.NR_NF == int(linha))
    rProxy = session.execute(stmt)
    result = rProxy.fetchall()
    file1 = open('./' + linha.rstrip('\n') + '.xml','w')
    file1.write(result[0][0].XML_NFE)
    file1.close()

arqAntecipacao.close()