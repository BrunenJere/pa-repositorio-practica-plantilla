import random

#Crea la lista llena de frases [frase,nombre]

def Lista_de_Frases():
    with open("frases_de_peliculas.txt","r",encoding= "UTF-8") as pelis:  
        frases= [] 
        frases_final= []
        for i in pelis:  
            frases.append(i)
        
        for x in range(len(frases)): 
            fras,nombre= frases[x].rstrip().split(";")  
            frases_final.append([fras,nombre])
    return frases_final        
            
def seleccion_frase(cantidad_de_runs): 
    #esta funcion selecciona azarosamente frases de peliculas, el nombre la pelicula a la que corresponde 
    #mas 2 opciones trampa
    frases_final=Lista_de_Frases()
    juego=[] 
    for i in range(cantidad_de_runs):   
        verdad = random.randint(1,len(frases_final)-1)   
        falsa1 = random.randint(1,len(frases_final)-1)   
        falsa2 = random.randint(1,len(frases_final)-1)   
        #verdad, falsa1, falsa2 son numeros al azar que luego, 
        #indicarán en qué indice de la lista general deberá buscar 
         
        frase_real,pelicula_real= frases_final[verdad]  
        desecho1,incorrecta1 = frases_final[falsa1] 
        desecho2,incorrecta2 = frases_final[falsa2]  
        #frase_real y pelicula_real son, la frase seleccionada al azar con la pelicula a la que corresponde
        #incorrecta1 e incorrecta2 son las peliculas que no corresponden a la frase 
        
        
        
        while frase_real == desecho1: 
              nuevo_numero = random.randint(1,len(frases_final))    
              desecho1_nuevo,incorrecta1 = frases_final[nuevo_numero]  
              desecho1 = desecho1_nuevo                
        while frase_real == desecho2: 
              nuevo_numero = random.randint(1,len(frases_final))    
              desecho2_nuevo,incorrecta1 = frases_final[nuevo_numero]  
              desecho2 = desecho2_nuevo        
        while pelicula_real == incorrecta1: 
              nuevo_numero = random.randint(1,len(frases_final))    
              desecho,incorrecta_nueva = frases_final[nuevo_numero]  
              incorrecta1 = incorrecta_nueva 
        while pelicula_real == incorrecta2: 
              nuevo_numero2 = random.randint(1,len(frases_final))    
              desecho,incorrecta_nueva2 = frases_final[nuevo_numero2]  
              incorrecta2 = incorrecta_nueva2
        #Con estos while me aseguro que el nombre de la pelicula no es igual a alguna de las opciones trampa,
        # ni las frases seleccionadas se repiten.
        
        juego.append([frase_real,pelicula_real,incorrecta1,incorrecta2])  
        
    return juego
     