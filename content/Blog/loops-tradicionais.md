Title: Loops 'tradicionais'
Date: 2012-11-1
Tags: 

Meu camarada [Irber](http://blog.luizirber.org/), relembrando como fazer um loop 'tradicionalista' onde se pegam os indices dos itens de uma lista ou de um numpy array, usando o enumerate, para pegar o valor e seu "indice".  
  
Buscando, dessa forma, um loop tradicionalista, porem mais pythonico (eu acho).  

    
    
    valores = ([1,3,5,7,9])
    for i, value in enumerate(valores):
        print i, value
    
    Out[2]:
    0 1
    1 3
    2 5
    3 7
    4 9
    

Sendo o jeito um tanto mais "conservador" e talvez menos pythonico:  

    
    
    for i in xrange(len(valores)):
        print i, valores[i]
    
    Out[4]:
    0 1
    1 3
    2 5
    3 7
    4 9
    

Ate mais. 
