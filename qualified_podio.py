def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3,nome_corredor1,nome_corredor2,nome_corredor3):
  
    # Implemente aqui a lógica da função
    if (tempo_chegada1 < tempo_chegada2) and (tempo_chegada2 < tempo_chegada3):
        menor = tempo_chegada1
        medio = tempo_chegada2
        maior = tempo_chegada3
        
        primeiro_nome = nome_corredor1
        segundo_nome = nome_corredor2
        terceiro_nome = nome_corredor3
        
    elif(tempo_chegada1 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada2):
        menor = tempo_chegada1
        medio = tempo_chegada3
        maior = tempo_chegada2
        
        primeiro_nome = nome_corredor1
        segundo_nome = nome_corredor3
        terceiro_nome = nome_corredor2
        
    elif(tempo_chegada2 < tempo_chegada1) and (tempo_chegada1 < tempo_chegada3):
        menor = tempo_chegada2
        medio = tempo_chegada1
        maior = tempo_chegada3
        
        primeiro_nome = nome_corredor2
        segundo_nome = nome_corredor1
        terceiro_nome = nome_corredor3
        
    elif(tempo_chegada2 < tempo_chegada3) and (tempo_chegada3 < tempo_chegada1):
        menor = tempo_chegada2
        medio = tempo_chegada3
        maior = tempo_chegada1
        
        primeiro_nome = nome_corredor2
        segundo_nome = nome_corredor3
        terceiro_nome = nome_corredor1
    elif(tempo_chegada3 < tempo_chegada2) and (tempo_chegada2 < tempo_chegada1):
        menor = tempo_chegada3
        medio = tempo_chegada2
        maior = tempo_chegada1
        
        primeiro_nome = nome_corredor3
        segundo_nome = nome_corredor2
        terceiro_nome = nome_corredor1
    elif(tempo_chegada3 < tempo_chegada1) and (tempo_chegada1 < tempo_chegada2):
        menor = tempo_chegada3
        medio = tempo_chegada1
        maior = tempo_chegada2
        
        primeiro_nome = nome_corredor3
        segundo_nome = nome_corredor1
        terceiro_nome = nome_corredor2
        
    return (f"1 - {primeiro_nome} - {menor} minutos\n"
            f"2 - {segundo_nome}  - {medio} minutos\n" 
            f"3 - {terceiro_nome} - {maior} minutos\n")
  
  
print(podio_olimpico(2,1,3,"Ronaldo","Wanderlei Cordeiro de Lima","Eliud Kipchoge"))