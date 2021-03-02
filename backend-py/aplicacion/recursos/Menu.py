#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys,os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from aplicacion.modelos.Menu import Menu

class MenuResource(Resource):

    def get(self):
        menu = []
        try:
            datos = Menu.getAll()
            if datos:
                for row in datos:
                    data = {
                        "id": row.id,
                        "name": row.name,
                        "icon": row.icon,
                        "url": row.url,
                        "submenu": row.submenu
                    }
                    
                    menu.append(data)
                        
            return {  "response":{"data": { "menu": menu }}}, 200
            

        except Exception as e:
            print(" ## Error ## \n")
            print(e)
            print("\n")
            return {"message": "Ha ocurrido un error de conexión." + e}, 500

