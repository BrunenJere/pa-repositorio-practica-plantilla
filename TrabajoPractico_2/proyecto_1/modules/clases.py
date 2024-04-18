    
class Facultad:  
    def __init__(self,nombre): 
        self.nombre = nombre
        self.lista_departamentos = []
        self.lista_alumnos = []
        self.lista_profesores = [] 
        
    def crear_departamentos(self,facultad,nombre_del_departamento,director):  
        nuevo_departamento = Departamento(facultad,nombre_del_departamento,director)
        self.lista_departamentos.append(nuevo_departamento)        
        
    def listar_departamentos(self): 
        print(f"Los departamentos actuales que presenta la facultad son: {[i.nombre_departamento for i in self.lista_departamentos]}")       
        
        
        
    def agregar_alumno(self,nuevo_alumno):  
        if isinstance(nuevo_alumno, Alumno):
            self.lista_alumnos.append(nuevo_alumno)  
        
    def listar_alumnos(self): 
        print(f"Los alumnos actuales en el sistema son: {[i.nombre for i in self.lista_alumnos]}")
        
        
             
    def contratar_profesor(self,nombre_profesor,dni_profesor,cargo):  
        nuevo_profesor = Profesor(nombre_profesor,dni_profesor,cargo) 
        if isinstance(nuevo_profesor, Profesor):
            self.lista_profesores.append(nuevo_profesor)    
        
    def listar_profesores(self): 
       print(f"Los profesores actuales en el sistema son: {[i.nombre for i in self.lista_profesores]}")
        

class Departamento: 
    def __init__(self,facultad,nombre_departamento,director): 
        self.facultad = facultad
        self.director = director  
        self.nombre_departamento = nombre_departamento 
        self.cursos = [] 
           
    def crear_curso(self,departamento,titular,nombre_curso): 
        nuevo_curso = Curso(departamento,titular,nombre_curso)  
        self.cursos.append(nuevo_curso)  
        
    def listar_cursos(self): 
        print(f"Los cursos disponibles en este departamento son: {[i.nombre_curso for i in self.cursos]}")
        
        
        
class Curso: 
    def __init__(self,departamento,titular,nombre_curso):  
        self.departamento = departamento
        self.titular = titular  
        self.nombre_curso = nombre_curso 
        self.participantes = [] 
        
    def inscribir_alumno(self,alumno):  
        if isinstance(alumno, Alumno):
            self.participantes.append(alumno)
            
            
class Profesor: 
    def __init__(self,nombre,dni,cargo):
        self.nombre = nombre 
        self._dni = dni  
        self.cargo = cargo
        
class Alumno: 
    def __init__(self,nombre,dni): 
        self.nombre = nombre 
        self._dni = dni  
        self.cargo = "Estudiante"