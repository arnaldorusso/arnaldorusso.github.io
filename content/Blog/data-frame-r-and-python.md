Title: Data Frame - R and Python
Date: 2013-1-28
Tags: 

Para acessar alguns dados com **R**, e poder realizar operaçoes, utilizamos a funçao **data.frame** podendo agrupando fatores entre outras operaçoes. Em Python a coisa pode ser bastante parecida e com diversas funcionabilidades do pacote **[Pandas](http://pandas.pydata.org/) [1]** para Python.  
  
Digamos uma tabela da seguinte maneira:  

    
    :::rconsole    
    ID sp1 sp2 sp3
    C1   1   3   2
    C1   3   2   0
    C1   2   1   1
    C2   2   4   0
    C2   1   3   1
    C3   0   3   4
    C3   2   1   2
    
O codigo para abrir como data.frame
    
    :::rconsole
    #! /usr/bin/R
    > dados = read.table('dados.txt', header=T)
    > dados
      ID sp1 sp2 sp3
    1 C1   1   3   2
    2 C1   3   2   0
    3 C1   2   1   1
    4 C2   2   4   0
    5 C2   1   3   1
    6 C3   0   3   4
    7 C3   2   1   2
    
    > attach(dados)
    
    # transformando a coluna ID em fator.
    > dados$ID <- as.factor(dados$ID)
    [1] 1 3 2 2 1 0 2

O que nao era necessario, pois ao carregar o data.frame o R ja´ reconhece essa coluna como factor.

    :::rconsole
    > str(dados)
    'data.frame':   7 obs. of  4 variables:
     $ ID : Factor w/ 3 levels "C1","C2","C3": 1 1 1 2 2 3 3
     $ sp1: int  1 3 2 2 1 0 2
     $ sp2: int  3 2 1 4 3 3 1
     $ sp3: int  2 0 1 0 1 4 2

para fazer uma media, por exemplo, utilizando o fator ID.

    :::rconsole
    > tapply(dados$sp1, dados$ID, mean)
     C1  C2  C3 
    2.0 1.5 1.0 
    
Para fazer isso em Python, voce poderia usar o **numpy**, simplesmente, ou usar as elegantes ferramentas do "pandas". Para quem vem do **R**, o **[Pandas](http://pandas.pydata.org/)** e uma forma facil de se entender com dados tabelados e cheios de fatores.  
    
    :::python    
    >>> import pandas as pd
    >>> dados = pd.read_table('dados.txt',sep=" ")
    >>> dados
       ID  sp1  sp2  sp3
    0  C1    1    3    2
    1  C1    3    2    0
    2  C1    2    1    1
    3  C2    2    4    0
    4  C2    1    3    1
    5  C3    0    3    4
    6  C3    2    1    2

Acessar somente uma das colunas.

    :::python
    >>> dados['sp1']
    0    1
    1    3
    2    2
    3    2
    4    1
    5    0
    6    2
    Name: sp1

Para fazer a media, com a funçao groupby
    
    :::python
    >>> dados.groupby('ID').sp1.mean()
    ID
    C1    2.0
    C2    1.5
    C3    1.0
    Name: sp1

Ainda e possivel fazer varias coisas com o objeto dados (que agora e um DataFrame).
Por exemplo, pegar a media e a variancia, ordenados por ID.

    :::python
    >>> dados.groupby('ID').sp1.agg(['mean', 'var'])
        mean  var
    ID           
    C1   2.0  1.0
    C2   1.5  0.5
    C3   1.0  2.0
    
Ate mais.  
[1] <http://pandas.pydata.org/>
