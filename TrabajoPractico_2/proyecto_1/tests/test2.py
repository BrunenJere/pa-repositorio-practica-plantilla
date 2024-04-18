# class Facultad:  
#     def __init__(self,nombre): 
#         self.nombre = nombre
#         self.lista_departamentos = []
#         self.lista_alumnos = []
#         self.lista_profesores = [] 
        
#     def agregar_departamentos(self,nuevo_departamento): 
#         self.lista_departamentos.append(nuevo_departamento)   
#         nuevo_departamento.director.cargo = "director"
           
        
#     def agregar_alumno(self,nuevo_alumno): 
#         self.lista_alumnos.append(nuevo_alumno)
        
#     def agregar_profesor(self,nuevo_profesor): 
#         self.lista_profesores.append(nuevo_profesor)  
        
        



# class Departamento: 
#     def __init__(self,facultad,director,nombre_departamento): 
#         self.facultad = facultad
#         self.director = director  
#         self.nombre_departamento = nombre_departamento
        

# class Curso: 
#     def __init__(self,departamento,titular,nombre_curso):  
#         self.departamento = departamento
#         self.titular = titular  
#         self.nombre_curso = nombre_curso
            

# class Profesor: 
#     def __init__(self,nombre,dni):
#         self.nombre = nombre 
#         self._dni = dni  
#         self.cargo = "profesor"
        
        
        
# class Alumno: 
#     def __init__(self,nombre,dni): 
#         self.nombre = nombre 
#         self._dni = dni  
#         self.cargo = "Estudiante"
       
        
        
# facultad_1 = Facultad("FIUNER")  






# alumno_1 = Alumno("jere",4545)
# alumno_2 = Alumno("viki",4848)
# alumno_3 = Alumno("valen",5151)

# profesor_1 = Profesor("Escher",1212)
# profesor_2 = Profesor("Lili",3030)
# profesor_3 = Profesor("Graciela",1020) 

# departamento_calculo = Departamento(facultad_1,profesor_2,"dpto. calculo") 

# curso_geometria = Curso(departamento_calculo,profesor_1,"geometria")


# facultad_1.agregar_profesor(profesor_1)
# facultad_1.agregar_profesor(profesor_2)
# facultad_1.agregar_profesor(profesor_3)

# facultad_1.agregar_alumno(alumno_1)
# facultad_1.agregar_alumno(alumno_2)
# facultad_1.agregar_alumno(alumno_3) 

# facultad_1.agregar_departamentos(departamento_calculo)




# print('''##########################################
#  #  Sistema de Información Universitaria  #
#  ##########################################
#  Elige una opción
#  1 - Inscribir alumno
#  2 - Contratar profesor
#  3 - Crear departamento nuevo
#  4 - Crear curso nuevo
#  5 - Inscribir estudiante a un curso
#  6 - Salir''')
# num=int(input('ingrese numero: '))
# while num!=6:
 
#     if num==1:
#          alumno_nuevo = Alumno(input("ingrese el nombre: "),input("ingrese el dni: ")) 
#          facultad_1.agregar_alumno(alumno_nuevo)      
#          print(f"los alumnos son: {[i.nombre for i in facultad_1.lista_alumnos]}")
         
#          #no se guarda cuando termina de correr
         
         
#     if num==2:
#          profe_nuevo = Profesor(input("ingrese el nombre: "),input("ingrese el dni: ")) 
#          facultad_1.agregar_profesor(profe_nuevo)          
#          print(f"los profes son: {[i.nombre for i in facultad_1.lista_profesores]}")
         
#          #tampoco
         
#     if num==3: 
        
#          profes_disponibles = []
#          for i in facultad_1.lista_profesores: 
#              if i.cargo == "profesor": 
#                 profes_disponibles.append(i.nombre)   
                 
#          if len(profes_disponibles) > 0:          
#             print(f"seleccione un profesor disponible: {[i for i in profes_disponibles]}")  
#             director = input("director del departamento: ").capitalize() 
#             for i in facultad_1.lista_profesores: 
#                 if i.nombre == director: 
#                     departamento_nuevo = Departamento(facultad_1,i,input("ingrese el nombre del departamento nuevo: ")) 
#                     facultad_1.agregar_departamentos(departamento_nuevo)

#             print(f"los departamentos son: {[i.nombre_departamento for i in facultad_1.lista_departamentos]}")
#          else: 
#              print("por ahora no hay profes disponibles") 
             
#         #tampoco 
     
     
#     if num==4:
#          print('crear curso nuevo')
#          pass
     
#     if num==5:
#          print('incribir estudiante a curso')
#          pass   
#     num=int(input('ingrese numero:')) 
    
# with open(f"./data/lista_de_info.txt","a", newline="") as archivo: 
    
#     archivo.write(f"{[i.nombre for i in facultad_1.lista_alumnos]}\n")










