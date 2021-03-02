import sys, os, re
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Index, Integer, String, Table, Text, Time
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.types import LONGBLOB
from sqlalchemy.dialects.mysql.enumerated import ENUM
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import func


# db = SQLAlchemy()

from aplicacion.db import db


class paciente(db.Model):
    __tablename__ = 'paciente'

    id = db.Column(db.Integer, primary_key=True)
    identificacion = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    fecNacimiento = db.Column(db.DateTime, nullable=False)
    idHistoriaClinica = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    direccion = db.Column(db.String(45), nullable=False)
    telefono = db.Column(db.String(45), nullable=False)
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
    def insert(cls, dataJson):
        query = ( 
                identificacion = dataJson["identificacion"],
                nombre = dataJson["nombre"],
                apellido = dataJson["apellido"],
                fecNacimiento = dataJson["fecNacimiento"],
                idHistoriaClinica = dataJson["idHistoriaClinica"],
                sexo = dataJson["sexo"],
                direccion = dataJson["direccion"],                
                telefono = dataJson["telefono"],                
            )
        paciente.guardar(query)
        if query.id:                            
            return  query.id 
        return  False

    @classmethod
    def update_data(cls, _id, dataJson):
        try:
            db.session.rollback()
            query = cls.query.filter_by(id=_id).first()
            if query:
                if "identificacion" in dataJson:
                    query.identificacion = dataJson["identificacion"]
                if "nombre" in dataJson:
                    query.nombre = dataJson["nombre"]
                if "apellido" in dataJson:
                    query.apellido = dataJson["apellido"]
                if "fecNacimiento" in dataJson:
                    query.fecNacimiento = dataJson["fecNacimiento"] 
                if "idHistoriaClinica" in dataJson:
                    query.idHistoriaClinica = dataJson["idHistoriaClinica"] 
                if "sexo" in dataJson:
                    query.sexo = dataJson["sexo"] 
                if "direccion" in dataJson:
                    query.direccion = dataJson["direccion"] 
                if "telefono" in dataJson:
                    query.telefono = dataJson["telefono"]                            

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

    @classmethod
    def Listar_Pacientes_Mayor_Riesgo(cls)
        try:
            sql = "SELECT "\
                "identificacion, nombre, apellido ,YEAR(CURDATE())-YEAR(paciente.fecNacimiento)+ IF(DATE_FORMAT(CURDATE(),'%m-%d') > DATE_FORMAT(paciente.fecNacimiento,'%m-%d'), 0 , -1 )AS edadActual"\
                "from pruebadesarrollo.paciente "               
        query = db.session.execute(sql)
        result = {}
        result["data"] = []
        if query:
            for row in query:
                dataRow = {
                            "identificacion": row["identificacion"],
                            "nombre": row["nombre"],
                            "apellido": str(row["apellido"]),
                            "edadActual": str(row["edadActual"]),                         
                        }
                result["data"].append(dataRow)

        return result    


     @classmethod
     def Listar_Pacientes_Fumadores_Urgentes(cls, _id)
        try:
            sql = "SELECT "\
                "paciente.identificacion, paciente.nombre ,pjoven.fumador, pjoven.edadFumador"\
                "from paciente inner join pjoven on paciente.idHistoraClinica= pjoven.idHistoriaClinica where paciente.idHistoraClinica=id=" + _id 
        query = db.session.execute(sql)
        result = {}
        result["data"] = []
        if query:
            for row in query:
                dataRow = {
                            "identificacion": row["identificacion"],
                            "nombre": row["nombre"],
                            "fumador": str(row["apellido"]),                                                
                        }
                result["data"].append(dataRow)

        return result 

    @classmethod
    def Paciente_mas_Anciano(cls)
        try:
            sql = "SELECT "\
                "identificacion, nombre,fecNacimiento"\
                "from paciente order by fecNacimiento asc limit 1" 
        query = db.session.execute(sql)
        result = {}
        result["data"] = []
        if query:
            for row in query:
                dataRow = {
                            "identificacion": row["identificacion"],
                            "nombre": row["nombre"],
                            "fecNacimiento": str(row["apellido"]),                                                
                        }
                result["data"].append(dataRow)

        return result 

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

