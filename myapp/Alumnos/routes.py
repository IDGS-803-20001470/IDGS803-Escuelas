from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
# import forms
from models import db

import forms

from flask import jsonify
# Se genera la configuracion de la base de datos
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db as db2
from flask_sqlalchemy import SQLAlchemy


from models import Alumnos
from db import get_connection
import json

alumnos = Blueprint('alumnos', __name__)
# db2 = SQLAlchemy(app)
csrf= CSRFProtect()


@alumnos.route('/getAlumn', methods=['GET', 'POST'])
def getAlumn():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            sql = "call getAlumnos()"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            
           
            # listar= json.dumps(lista)

           
            connection.close()
            

    except Exception as e:
        print("Error: ", e)
        pass

    return render_template('ABCompletoAlum.html', alumnos=resultset)


@alumnos.route('/eliminarAlumn', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        idAlumno = request.args.get('id')
        print("idAlumno ", idAlumno)
        try:
            connection = get_connection()
            with connection.cursor() as cursor:

                cursor.execute('call getAlumnos2(%s)', (idAlumno,))
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                connection.close()
                create_form.id.data=resultset[0][0]
                create_form.nombre.data=resultset[0][1]
                create_form.apellidos.data=resultset[0][2]
                create_form.email.data=resultset[0][4]
              


        except Exception as e:
            print("Error 1: ", e)
            pass

    #alum1 = db2.session.query(Alumnos).filter(Alumnos.id == idAlumno).first()

    # Creamos el formulario con los datos del alumno
        
        return render_template('eliminarAlum.html', form=create_form, alumnos=resultset)
    
    if request.method == 'POST':

        id = create_form.id.data
        print("id ELIMINAR ", id)

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                try:   
                    cursor.execute('call deleteAlumno(%s)', (id,))

                   # connection.close()
                
                finally:
                    connection.commit()
              
        except Exception as e:
            print("Error 2: ", e)
            pass
        print("RUTA")
        return redirect(url_for('alumnos.getAlumn'))
        #return render_template('eliminarAlum.html', form=create_form, alumnos=resultset)
    return render_template('eliminarAlumn.html', form=create_form)




@alumnos.route('/crearAlum', methods=['GET','POST'])
def crear():
    create_form=forms.UserForm(request.form)
    
    if(request.method=='GET'):
        return render_template('crearAlum.html', form=create_form)
    
    
    if request.method=='POST' and create_form.validate():
        alumno=Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data
        )
        print("alumno ", alumno)
        
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                try:   
                    cursor.execute('call addAlumno(%s, %s, %s)', (alumno.nombre,alumno.apellidos,alumno.email,))

                   # connection.close()
                
                finally:
                    connection.commit()
              
        except Exception as e:
            print("Error 2: ", e)
            pass
        print("RUTA")
        return redirect(url_for('alumnos.getAlumn'))
    
    return render_template('crearAlum.html', form=create_form)



@alumnos.route('/modificarAlumn', methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        idAlumno = request.args.get('id')
        print("idAlumno ", idAlumno)
        try:
            connection = get_connection()
            with connection.cursor() as cursor:

                cursor.execute('call getAlumnos2(%s)', (idAlumno,))
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                connection.close()
                create_form.id.data=resultset[0][0]
                create_form.nombre.data=resultset[0][1]
                create_form.apellidos.data=resultset[0][2]
                create_form.email.data=resultset[0][4]
              


        except Exception as e:
            print("Error 1: ", e)
            pass

    #alum1 = db2.session.query(Alumnos).filter(Alumnos.id == idAlumno).first()

    # Creamos el formulario con los datos del alumno
        
        return render_template('modificarAlum.html', form=create_form, alumnos=resultset)
    
    if request.method == 'POST':

        id = create_form.id.data
        print("id ELIMINAR ", id)
        alumno=Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data
        )

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                try:   
                    cursor.execute('call editAlumno(%s,%s,%s,%s)', (id, alumno.nombre,alumno.apellidos,alumno.email,))

                   # connection.close()
                
                finally:
                    connection.commit()
              
        except Exception as e:
            print("Error 2: ", e)
            pass
        print("RUTA")
        return redirect(url_for('alumnos.getAlumn'))
        #return render_template('eliminarAlum.html', form=create_form, alumnos=resultset)
    return render_template('modificarAlum.html', form=create_form)
