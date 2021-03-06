# coding: utf-8

import sys, os, re
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Index, Integer, String, Table, Text, Time
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.types import LONGBLOB
from sqlalchemy.dialects.mysql.enumerated import ENUM
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import func


# db = SQLAlchemy()

from aplicacion.db import db


class pjoven(db.Model):
    __tablename__ = 'pjoven'

    id = db.Column(db.Integer, primary_key=True)
    fumador = db.Column(db.Integer, nullable=False)
    idHistoriaClinica = db.Column(db.Integer, nullable=False)
    edadFumador = db.Column(db.Integer, nullable=False)
    #CRUD

    @classmethod
    def getAll(cls):
        query =  cls.query.all()
        return query

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(id=_id).first()
        return query
    
    @classmethod
    def getFumadorPorHistoria(cls, _id):
        query =  cls.query.filter_by(idHistoriaClinica=_id).first()
        return query

    @classmethod
    def insert(cls, dataJson):
        query = (                 
                fumador = dataJson["fumador"], 
                idHistoriaClinica = dataJson["idHistoriaClinica"], 
                edadFumador = dataJson["edadFumador"],               
            )
        pjoven.guardar(query)
        if query.id:                            
            return  query.id 
        return  False

    @classmethod
    def update_data(cls, _id, dataJson):
        try:
            db.session.rollback()
            query = cls.query.filter_by(id=_id).first()
            if query:
                if "fumador" in dataJson:
                    query.fumador = dataJson["fumador"]
                if "idHistoriaClinica" in dataJson:
                    query.idHistoriaClinica = dataJson["idHistoriaClinica"]
                if "edadFumador" in dataJson:
                    query.edadFumador = dataJson["edadFumador"]
                                   
                query.updated_at = func.NOW()
                db.session.commit()
                if query.id:                            
                    return query.id
            return  None
        except Exception as e:
            print("=======================E")
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            msj = 'Error: '+ str(exc_obj) + ' File: ' + fname +' linea: '+ str(exc_tb.tb_lineno)
            return {'mensaje': str(msj) }, 500



    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

