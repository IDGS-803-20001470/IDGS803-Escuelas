from flask import Blueprint
    
from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
#import forms 

from flask import jsonify
from config import DevelopmentConfig #Se genera la configuracion de la base de datos
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Profesores
from db import get_connection
import forms


maestros=Blueprint('maestros', __name__)

@maestros.route('/getProfe', methods=['GET', 'POST'])
def getMaes():
    try:    
        connection= get_connection()
        with connection.cursor() as cursor:
            sql = "call getProfesores()"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            for row in resultset:
                print(row)
            print(list(resultset))
            lista= list(resultset)
            #listar= json.dumps(lista)
           
        
    except Exception as e:
        print("Error: ", e)
        pass
    
    #create_form=forms.UserForm(request.form)
    #alumnos=Alumnos.query.all()
   
    return render_template('ABCompletoProf.html', profesores=resultset)



@maestros.route('/eliminarProf', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.MaestrosForm(request.form)

    if request.method == 'GET':
        idProfesor = request.args.get('id')
        print("idProfe ", idProfesor)
        try:
            connection = get_connection()
            with connection.cursor() as cursor:

                cursor.execute('call getProfesores2(%s)', (idProfesor,))
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                connection.close()
                create_form.id.data=resultset[0][0]
                create_form.nombre.data=resultset[0][1]
                create_form.apellidos.data=resultset[0][2]
                create_form.email.data=resultset[0][4]
                create_form.materia.data=resultset[0][5]
              


        except Exception as e:
            print("Error 1: ", e)
            pass

    #alum1 = db2.session.query(Alumnos).filter(Alumnos.id == idAlumno).first()

    # Creamos el formulario con los datos del alumno
        
        return render_template('eliminarProf.html', form=create_form)
    
    if request.method == 'POST':

        id = create_form.id.data
        print("id ELIMINAR ", id)

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                try:   
                    cursor.execute('call deleteProfe(%s)', (id,))

                   # connection.close()
                
                finally:
                    connection.commit()
              
        except Exception as e:
            print("Error 2: ", e)
            pass
        print("RUTA")
        return redirect(url_for('maestros.getMaes'))
        #return render_template('eliminarAlum.html', form=create_form, alumnos=resultset)
    return render_template('eliminarProf.html', form=create_form)




@maestros.route('/crearProf', methods=['GET','POST'])
def crear():
    create_form=forms.MaestrosForm(request.form)
    
    if(request.method=='GET'):
        return render_template('crearProf.html', form=create_form)
    
    
    if request.method=='POST' and create_form.validate():
        profe= Profesores(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            materia= create_form.materia.data,
        )
        print("Profesores ", Profesores)
        
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                try:   
                    cursor.execute('call addProfe(%s, %s, %s, %s)', (profe.nombre,profe.apellidos,profe.email,profe.materia,))

                   # connection.close()
                
                finally:
                    connection.commit()
              
        except Exception as e:
            print("Error 2: ", e)
            pass
        print("RUTA")
        return redirect(url_for('maestros.getMaes'))
    
    return render_template('crearProf.html', form=create_form)



@maestros.route('/modificarProf', methods=['GET', 'POST'])
def modificar():
    create_form = forms.MaestrosForm(request.form)

    if request.method == 'GET':
        idProfe = request.args.get('id')
        print("idProfe ", idProfe)
        try:
            connection = get_connection()
            with connection.cursor() as cursor:

                cursor.execute('call getProfesores2(%s)', (idProfe,))
                resultset = cursor.fetchall()
                for row in resultset:
                    print(row)
                connection.close()
                create_form.id.data=resultset[0][0]
                create_form.nombre.data=resultset[0][1]
                create_form.apellidos.data=resultset[0][2]
                create_form.email.data=resultset[0][4]
                create_form.materia.data=resultset[0][5]



        except Exception as e:
            print("Error 1: ", e)
            pass

    #alum1 = db2.session.query(Alumnos).filter(Alumnos.id == idAlumno).first()

    # Creamos el formulario con los datos del alumno
        
        return render_template('modificarProf.html', form=create_form)
    
    if request.method == 'POST':

        id = create_form.id.data
        print("id ELIMINAR ", id)
        profe=Profesores(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            materia=create_form.materia.data
        )

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                try:   
                    cursor.execute('call editProfe(%s,%s,%s,%s,%s)', (id, profe.nombre,profe.apellidos,profe.email,profe.materia,))

                   # connection.close()
                
                finally:
                    connection.commit()
              
        except Exception as e:
            print("Error 2: ", e)
            pass
        print("RUTA")
        return redirect(url_for('maestros.getMaes'))
        #return render_template('eliminarAlum.html', form=create_form, alumnos=resultset)
    return render_template('modificarProf.html', form=create_form)
    