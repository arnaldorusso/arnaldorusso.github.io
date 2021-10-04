Title: O amor tambem fala Python
Date: 2013-11-18
Tags: 

Encontrei uma maneira elegante para dizer " Baixinha, eu te amo!"  
Claro que e um tanto Pythonico, mas como o amor pode ser expresso em qualquer linguagem, por que nao em Python?  

    
    :::python    
    In  [3]: Baixinha(eu[te <3 ])
    Out [3]: 'E eh inf!' 

Eu digo, "Baixinha eu te amo"
    
    
Como eu sou muito amigo do Python... ele ja sabe disso e complementa.
**"E eh infinito"!**
    
    
Como o minimo de amor que ela aceita e um **<3** , escrevi uma funçao Python para isso.
    
    
    :::python    
    import numpy as np
    
    eu = 'eu'
    te = 'te'
    
    def Baixinha(val):
        if val < '<3':
            raise ReferenceError
        else:
            return 'E eh %f!' % np.inf


![](images/github_pythocat.png)   
