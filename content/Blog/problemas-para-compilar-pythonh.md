Title: Problemas para compilar. Python.h
Date: 2012-5-5
Tags: 

Estava encontrando erro (Python.h: No such file or directory), para varios arquivos distintos, dependendo do pacote que ia instalar com o **pip**.  
  
Fiz uma busca e nao encontrei respostas para os pacotes que apresentavam problemas na compilaçao.  
Em especifico para a instalaçao do Pyclimate em uma das maquinas.  

    
    
    src/JDTime_wrap.c:44:20: fatal error: Python.h: Arquivo ou diretorio nao encontrado
    

  
Para resolver isso:  

    
    
    #!/bin/bash
    aptitude install python-dev
    

Instalara os headers e voce podera compilar normalmente.  
Espero que ajude! 
