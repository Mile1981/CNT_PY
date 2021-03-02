#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import json
import sys,os
import datetime
import requests
from flask import Flask, request, jsonify, session
from flask_restful import Resource, reqparse
from unidecode import unidecode
from aplicacion.app import app_config, enviroment
from aplicacion.modelos.paciente import paciente
from aplicacion.modelos.pninno import pninno
from aplicacion.modelos.pjoven import pjoven
from aplicacion.modelos.panciano import panciano


#Se recibe el número de HC y se listan los pacientes con mayor riesgo que el paciente al cual pertenece el # de HC ingresado
class Listar_Pacientes_Mayor_Riesgo(Resource): 
    def get(self): 
        data = request.json            
        idHC = data["idHistoriaClinica"]
        lista_Paciente = []   
        prioridad = 0
        riesgoporPaciente = 0
        riesgoFiltro = 0
        try:
        datos = paciente.Listar_Pacientes_Mayor_Riesgo()
        for dpaciente in datos:         
            if dpaciente.edadActual >=1 and dpaciente.edadActual <=5:
                prioridad = pninno.getPesoEstaturaPorHistoria(paciente.idHistoriaClinica) + 3                
            if dpaciente.edadActual >=6 and dpaciente.edadActual  <= 12:
                prioridad = pninno.getPesoEstaturaPorHistoria(paciente.idHistoriaClinica) + 2                
            if dpaciente.edadActual >=13 and dpaciente.edadActual  <= 15:
                prioridad = pninno.getPesoEstaturaPorHistoria(paciente.idHistoriaClinica) + 1
            if dpaciente.edadActual >=16 and dpaciente.edadActual <= 40:
                prioridad = (pjoven.getFumadorPorHistoria(paciente.idHistoriaClinica)/4 ) + 2
            if dpaciente.edadActual >41 :
                if panciano.getDietaPorHistoria(paciente.idHistoriaClinica):
                    prioridad = dpaciente.edadActual/20 + 4
                else:
                    prioridad = dpaciente.edadActual/30 + 3
                riesgoporPaciente = ((dpaciente.edadActual * prioridad) / 100)+ 5.3

            riesgoporPaciente = (dpaciente.edadActual * prioridad) / 100)

            data={
                "identificacion": paciente.identificacion,
                "idHistoriaClinica": paciente.idHistoriaClinica,
                "nombre": paciente.nombre,
                "apellido": paciente.apellido,
                "edadActual":paciente.edadActual,
                "prioridad":prioridad,
                "riesgo": riesgo
            }

            if data["idHistoriaClinica"] = idHC:
                riesgoFiltro = data["riesgo"]

            lista_Paciente.append(data)

            for paciente in lista_Paciente:
                if paciente["riesgo"] < riesgoFiltro
                    lista_Paciente.pop(paciente)

            return {"response":{"data": { "pacientes": lista_Paciente }}}, 200
         
        except Exception as e:            
            return {"message": "Ha ocurrido un error de conexión."  + e}, 500


#Se atiende al paciente de acuerdo a unos parámetros establecidos
class Atender_Paciente(Resource): 
    def get(self):
    
        try:

        except Exception as e:            
            return {"message": "Ha ocurrido un error de conexión."  + e}, 500

#Libera todas las consultas que están ocupadas
class Liberar_Consultas(Resource): 
    def get(self):
    
        try:

        except Exception as e:            
            return {"message": "Ha ocurrido un error de conexión."  + e}, 500

#Lista el nombre de los pacientes fumadores que requieren ser atendidos con urgencia
class Listar_Pacientes_Fumadores_Urgentes(Resource): 
    def get(self):
        paciente = []
        try:
        datos = paciente.Listar_Pacientes_Fumadores_Urgentes()
        if datos.fumador == 1:
            fumador=(datos.edadFumador/4) +2
        else:
            fumador=2
        except Exception as e:            
            return {"message": "Ha ocurrido un error de conexión."  + e}, 500

#Muestra la consulta que más pácientes ha atendido 
class Consulta_mas_Pacientes_Atendidos(Resource): 
    def get(self):
    
        try:

        except Exception as e:            
            return {"message": "Ha ocurrido un error de conexión."  + e}, 500

#Muestra los pacientes más ancianos de todos en la sala de espera
class Paciente_mas_Anciano(Resource): 
    def get(self):
        paciente = []
        try:
        datos = paciente.Listar_Pacientes_Fumadores_Urgentes()

        except Exception as e:            
            return {"message": "Ha ocurrido un error de conexión."  + e}, 500

#Optimiza la atención del paciente primero de mayor gravedad, en orden de urgencia seatenderán primero,, niños y ancianos con 
#prioridad y orden de llegada y por último los que se encuentren menos enfermos.
class Optimizar_Atencion(Resource): 
    def get(self):
    
        try:

        except Exception as e:            
            return {"message": "Ha ocurrido un error de conexión."  + e}, 500