from modules.modulo1 import tomar_datos
from modules.clases import Alumno,Facultad

        
        
facultad_1 = Facultad("FIUNER")  
alumnos,profesores,departamentos,cursos = tomar_datos("lista_de_info.txt") 
for alumno in alumnos: 
    ingresante = Alumno(alumno[0],alumno[1])  
    facultad_1.agregar_alumno(ingresante) 
for profesor in profesores: 
    facultad_1.contratar_profesor(profesor[0],profesor[1],profesor[2])   
for departamento in departamentos: 
    facultad_1.crear_departamentos(facultad_1,departamento[0],departamento[1])  
for curso in cursos: 
    for dpto in facultad_1.lista_departamentos: 
        if dpto.nombre_departamento == curso[0]:   
            for profe in facultad_1.lista_profesores: 
                if profe.nombre == curso[1]:
                    dpto.crear_curso(dpto,profe,curso[2])
    




print('''##########################################
 #  Sistema de Información Universitaria  #
 ##########################################
 Elige una opción
 1 - Inscribir alumno
 2 - Contratar profesor
 3 - Crear departamento nuevo
 4 - Crear curso nuevo
 5 - Inscribir estudiante a un curso
 6 - Salir''')



while True: 
    num=input('ingrese numero: ') 
    try: 
        num = int(num) 
        break
    except ValueError: 
        print("ingrese un numero: ") 
        

while num != 6:
 
    if num==1:
        alumno_nuevo = Alumno(input("ingrese el nombre: ").capitalize(),input("ingrese el dni: ")) 
        facultad_1.agregar_alumno(alumno_nuevo)    
        print(f"El alumno {alumno_nuevo.nombre} fue inscrito en {facultad_1.nombre}")
        facultad_1.listar_alumnos()
        
         
         
         
    if num==2:
        facultad_1.contratar_profesor(input("ingrese el nombre: ").capitalize(),input("ingrese el dni: "),"Profesor")  
        print("El profesor ha sido contratado")
        facultad_1.listar_profesores()
        
         
         
    if num==3:        
        profes_disponibles = []
        for profe in facultad_1.lista_profesores: 
            if profe.cargo == "Profesor": 
               profes_disponibles.append(profe.nombre)   
                 
        if len(profes_disponibles) > 0:          
            director = input(f"seleccione un profesor disponible para ser director: {[profesor for profesor in profes_disponibles]}: ").capitalize()  
            for i in facultad_1.lista_profesores: 
                if i.nombre == director:  
                    i.cargo = "Director"
                    facultad_1.crear_departamentos(facultad_1,input("nombre del dpto: ").capitalize(),i) 
            facultad_1.listar_departamentos()
            
        else: 
            print("por ahora no hay profes disponibles para ser Director de departamento") 
            
        
     
    if num==4:
        profes_disponibles = []
        for profe in facultad_1.lista_profesores: 
            if profe.cargo == "Profesor": 
               profes_disponibles.append(profe.nombre)  
               
        if len(profes_disponibles) > 0:       
            departamento_perteneciente = input(f"seleccione un departamento para crear un curso: {[dpto.nombre_departamento for dpto in facultad_1.lista_departamentos]}: ").capitalize()
            titular_del_curso = input(f"Seleccione un profesor para ser titular: {[profe for profe in profes_disponibles]}:  ").capitalize() 
            for profe_seleccionado in facultad_1.lista_profesores:  
                if profe_seleccionado.nombre == titular_del_curso:  
                    profe_seleccionado.cargo = "Titular"
                    titular_del_curso = profe_seleccionado

            for dpto in facultad_1.lista_departamentos: 
                if dpto.nombre_departamento == departamento_perteneciente: 
                    dpto.crear_curso(departamento_perteneciente,titular_del_curso,input("nombre del curso: ").capitalize()) 
                    dpto.listar_cursos()
        else: 
            print("No hay profesores disponibles para ser Titular de curso")
        
         
         
         
    if num==5:
        inscrito = input(f"los alumnos en el sistema son: {[alumno.nombre for alumno in facultad_1.lista_alumnos]}: ").capitalize() 
        cursos_disponibles = [] 
        for departamento in facultad_1.lista_departamentos: 
            for curso in departamento.cursos: 
                cursos_disponibles.append(curso.nombre_curso) 
                
        if len(cursos_disponibles) > 0:            
            curso_seleccionado = input(f"los cursos disponibles son, seleccione uno: {[curso for curso in cursos_disponibles]}: ").capitalize()
            for departamento in facultad_1.lista_departamentos: 
                for curso in departamento.cursos:  
                    if curso_seleccionado == curso.nombre_curso: 
                        for alumno in facultad_1.lista_alumnos: 
                            if alumno.nombre == inscrito: 
                                curso.inscribir_alumno(alumno) 
                                print(f"{[i.nombre for i in curso.participantes]}") 
                                
        else: 
            print("No hay cursos disponibles para inscribirse")                        
        
                
                
    num=int(input('ingrese numero:')) 
    

   
cargo = [i.cargo for i in facultad_1.lista_profesores]   
for i in facultad_1.lista_alumnos: 
    cargo.append(i.cargo)  
        
nombre = [i.nombre for i in facultad_1.lista_profesores]  
for i in facultad_1.lista_alumnos: 
    nombre.append(i.nombre)
    
dni = [i._dni for i in facultad_1.lista_profesores]  
for i in facultad_1.lista_alumnos: 
    dni.append(i._dni) 
    

with open(f"./data/lista_de_info.txt","w", newline="") as archivo: 
    for i in range(len(facultad_1.lista_alumnos)+len(facultad_1.lista_profesores)):
        archivo.write(f"{cargo[i]},{nombre[i]},{dni[i]}\n")
        
    for i in range(len(facultad_1.lista_departamentos)): 
        archivo.write(f"Departamento,{facultad_1.lista_departamentos[i].nombre_departamento},{facultad_1.lista_departamentos[i].director}\n")    

    for i in facultad_1.lista_departamentos:   
        for j in i.cursos : 
            archivo.write(f"{i.nombre_departamento},{j.titular.nombre},{j.nombre_curso}\n")
            
            
            
        
