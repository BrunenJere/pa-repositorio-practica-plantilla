# módulo para organizar funciones o clases utilizadas en nuestro proyecto
def tomar_datos(archivo): 
    with open(f"data\{archivo}","r") as archivo:
        base_de_datos = archivo.readlines()   
        alumnos = []
        profesores = [] 
        departamentos = []
        cursos = []
        
        for i in base_de_datos:  
            cargo,nombre,dni = i.split(",") 
            if cargo == "Estudiante": 
                alumnos.append([nombre,dni.strip()]) 
            elif cargo == "Departamento": 
                departamentos.append([nombre,dni.strip()])
            elif cargo in ["Profesor","Titular","Director"]: 
                profesores.append([nombre,dni.strip(),cargo])   
            else: 
                cursos.append([cargo,nombre,dni.strip()])
        
    return alumnos,profesores,departamentos,cursos  


def obtener_base_de_datos(archivo,rol_institucional): 
    with open(f"./data/{archivo}","r") as archivo:
            archivo = archivo.readlines() 
            agentes_institucionales_actuales = [] 
            
            if rol_institucional == "Estudiante": 
                for renglon in archivo: 
                    cargo,nombre,dni = renglon.split(",")
                    if cargo == rol_institucional: 
                        agentes_institucionales_actuales.append(nombre)            
            
            if rol_institucional == "Profesor": 
                for renglon in archivo: 
                    cargo,nombre,dni = renglon.split(",") 
                    if cargo in ["Profesor","Titular","Director"]: 
                        agentes_institucionales_actuales.append(nombre)          
                        
            if rol_institucional ==  "Departamento": 
                for renglon in archivo: 
                    cargo,nombre,dni = renglon.split(",") 
                    if cargo == rol_institucional: 
                        agentes_institucionales_actuales.append(nombre)
            
                    
            
            
    return agentes_institucionales_actuales                
    