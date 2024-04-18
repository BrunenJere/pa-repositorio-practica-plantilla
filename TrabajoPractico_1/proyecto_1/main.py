# Aplicación principal
from modules.modulo1 import comprobar_cant_de_frases, listar_frases_alfabeticamente, seleccionar_frases_de_juego, obtener_fecha_actual,desordenar_opciones, generar_grafica, generar_grafica_torta, guardar_historial_jugadas, guardar_informacion_de_juego  
from modules.config import app
from flask import render_template,redirect, request, session




@app.route("/", methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        session['Nombre']= request.form['Nombre']
        session['Juegos']= request.form['Juegos']
        session['Juegos']=comprobar_cant_de_frases(session['Juegos'])
        session['intentos']=0
        session['fecha_actual']=obtener_fecha_actual()
        session['aciertos']=0
        session["Frases"]=seleccionar_frases_de_juego(int(session['Juegos']))         
        return redirect('/jugar')
    
    return render_template("inicio.html")
#pantalla de inicio; aquí se guardan todos los datos necesarios.
 
@app.route("/jugar", methods=["GET","POST"])
def jugar():
    session['intentos']+=1
    if session['intentos']<= int(session['Juegos']):    
        juego_actual={
            'frase':session['Frases'][session['intentos']-1][0],
            'opcion1':session['Frases'][session['intentos']-1][1],
            'opcion2':session['Frases'][session['intentos']-1][2],
            'opcion3':session['Frases'][session['intentos']-1][3],}
        #diccionario que guarda la pregunta y opciones a realizar en la ronda
        
        opciones_lista = [juego_actual["opcion1"], juego_actual['opcion2'], juego_actual['opcion3']] 
        opciones_lista=desordenar_opciones(opciones_lista)
        
        if request.method =='POST':
            respuestacorrecta=session['Frases'][session['intentos']-2][1]
            respuesta = request.form['respuesta']
            session["intentos"] -= 1
            if respuesta == respuestacorrecta:
                session['aciertos'] += 1
                return render_template("correcciones.html", test="acierto") 
            
            else:
                return render_template("correcciones.html", test="fallo", correcta=respuestacorrecta) 
        #este if es utilizado para poder comparar la respuesta con la opcion correcta
              
        return render_template("jugar.html", frase= juego_actual['frase'], opcion1= opciones_lista[0], opcion2= opciones_lista[1], opcion3= opciones_lista[2]) 
    else:
        if request.method =='POST':
            respuestacorrecta=session['Frases'][session['intentos']-2][1]
            respuesta = request.form['respuesta']
            session["intentos"] -= 1
            if respuesta == respuestacorrecta:
                session['aciertos'] += 1
                return render_template("correcciones.html", test="acierto")             
            #este if es utilizado para poder comparar la respuesta con la opcion correcta de la ultima frase
            else:
                return render_template("correcciones.html", test="fallo", correcta=respuestacorrecta) 
        guardar_informacion_de_juego(session['Nombre'],session['Juegos'],session['intentos']-1,session['fecha_actual'],session['aciertos'])
        return render_template("resultados.html",aciertos_actuales=session['aciertos'], Juegos=session['Juegos'])
#pantalla de juego, muestra las preguntas y opciones


@app.route("/resultados")
def resultados():
    return render_template("inicio.html")
#pantalla para mostrar resultados de la partida jugada

@app.route("/correcciones") 
def correcciones(): 
    return render_template("correcciones.html")
#muestra la correccion de las respuestas

@app.route("/graficos", methods=['GET', 'POST'])
def graficos():
    generar_grafica('.png')
    generar_grafica_torta('.png')
    if request.method=='POST':
        generar_grafica('.pdf')
        generar_grafica_torta('.pdf')   
    return render_template("graficos.html")
#genera los graficos actualizados, ademas permite descargar los graficos en formato pdf

@app.route("/historial")
def historial():
    nombres_datos_para_lista = guardar_historial_jugadas()
    return render_template("historial.html", datos=nombres_datos_para_lista)    
#pantalla con los resultados historicos

@app.route("/listado_pelis")
def listar():
    Lista_pelis_def=listar_frases_alfabeticamente("frases_de_peliculas.txt")  
    return render_template("listado_pelis.html",peliculas=Lista_pelis_def)
#pantalla con el listado de peliculas en el juego

if __name__ == "__main__":
    app.run(debug=True)