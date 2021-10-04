Title: Ler dados binários de gelo marinho com Python
Date: 2012-2-8
Tags: python numpy

Estava com erros ao ler arquivos binarios de medias mensais de gelo marinho, conseguidos atraves do site:  
<ftp://sidads.colorado.edu/DATASETS/seaice/polar-stereo/bootstrap/final-gsfc/south/monthly>  
  
  
  

    
    
    import numpy as np
    import matplotlib.pyplot as plt
    from glob import glob
    from scipy.io import loadmat
    # Lista de arquivos binarios
    d = sorted(glob('bt*'))
    # pegando somente um dos arquivos para leitura
    f = open(d[0],'rb')
    map1 = np.fromfile(f, dtype=np.uint16).reshape(316,332)
    f.close()
    im = map1.T/10.
    SI3[:,:,i] = im
    # Exemplo de linha do arquivo. Essa e a menor delas. 
    len(a) = 70.
    a = f.readlines()[1] 
    Out [2]: '\x03\x18\x03,\x03C\x03G\x03R\x03i\x03d\x03q\x03\x88\x03\x87\x03\x9a\
    
    
    x03\xbd\x03\xbd\x03\xb8\x03\xbd\x03\xc0\x03\xbf\x03\xc5\x03\xb5\x03\xa2\x03\x85
    
    
    \x03[\x03N\x03B\x03\x1a\x03\xeb\x02\xc4\x02\x95\x02\x94\x02p\x02w\x02X\x02H\x02.\x02\n'

  
  
Sabia que estava errando alguma coisa, pois ao plotar em um mapa, esses dados, eles ficavam assim:  
  



![](http://2.bp.blogspot.com/-62iv06DSDfA/TzLLOKm9BAI/AAAAAAAAADU/sfN9I2gCaw0/s640/testepy.png)

Figura tosca dos dados de Gelo.
Depois de muito quebrar a cabeça, analisando pedaços da matriz e comparando com um arquivo que tinha certo, vi que parecia estar faltando algo da codificaçao.  
De fato, isso se dava ao reshape que fazia ao final de fazer a leitura com o **np.fromfile**.  
O que acontece, e que por falta de informaçoes sobre esses dados, nao sabia como eles estava encapsulados. A unica informaçao que tinha e que deveriam ser lidos de 2 em 2 bytes ( o que e justificado pelo **dtype = np.uint16** ).  
Mas, como sabia que estava errado, varri a rede buscando alguma informaçao mais efetiva sobre isso.  
Muito falaram sobre o modulo struct [[link da dica 1](http://stackoverflow.com/questions/2865996/reading-a-binary-file-in-python-into-a-struct)], mas que nao consegui progredir por esse caminho.  
Comecei a verificar detalhadamente cada parte do codigo, que tinha, e acabei descobrindo de onde vinha o problema! =]). Tudo estava centrado na questao de que o NumPy faz um reshape nas matrizes de acordo com referencias em C e ou FORTRAN.  
  

    
    
     reshape(a, newshape, order='C'):
        """
        Gives a new shape to an array without changing its data.
    
        Parameters
        ----------
        a : array_like
            Array to be reshaped.
        newshape : int or tuple of ints
            The new shape should be compatible with the original shape. If
            an integer, then the result will be a 1-D array of that length.
            One shape dimension can be -1. In this case, the value is inferred
            from the length of the array and remaining dimensions.
        order : {'C', 'F'}, optional
            Determines whether the array data should be viewed as in C
            (row-major) order or FORTRAN (column-major) order.
    
    

Li isso tudo muito rapido e fui testar... Coloquei um order=True e FUNCIONOU! (Acho que por sorte mesmo.) Agora esta mudado para order='F', onde o meu dado "passa bem, sem remedios nem cirurgia".  

    
    
    A saida que obtinha era:
    
    
    
    
    
    
    
    
    In [5]: map1[:,123]
    Out [6]:
    array([1200, 1200, 1200, 1200, 1200, 1200,  712,  870,  928,  958,  957,
            974,  969,  983,  984,  979,  976,  978,  976,  977,  978,  979,
            982,  986,  988,  988,  993,  988,  990,  987,  997,  993,  991,
            995,  997,  990,  986,  992,  989,  993,  990,  975,  985,  979,
            979,  988,  976,  984,  970,  958,  962,  956,  941,  907,  841,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,  829,  845,
            774,  583,  486,  474,  557,  681,  774,  824,  840,  857,  861,
            862,  848,  838,  821,  784,  747,  689,  605,  522,  529,  500,
            468,  469,  470,  437,  414,  361,  360,  288,  236,  205,  151,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,  191,
            326,  590,  832,  914,  915,  950,  935, 1200,  951, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200,  695,  890,  945,  973,  960,  956,  972,
            976,  976])
    
    
    Essa saida, e muito diferente da saida correta, que se consegue com o processamento, incluindo o order='F'.
    
    
    In [7]: map1[:,123]
    Out [8]:
    array([1200, 1200, 1200, 1200, 0, 1200, 1200, 1200, 0, 0, 0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,  104,  228,
            301,  389, 1200,  519, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200,  651,  703,  748,  742,  739,  777,  831,
            915,  958,  965,  978,  988,  984,  988,  991,  989,  986,  986,
            986,  987,  983,  990,  989,  980,  985,  986,  980,  980,  974,
            971,  968,  980,  988,  983,  991,  991,  992,  990,  982,  978,
            973,  987,  989,  993,  987,  980,  977,  980,  982,  981,  984,
            976,  978,  965,  948,  937,  920,  881,  846, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200,
           1200,  852,  845,  852,  806,  657,  630,  554,  573,  621,  682,
            738,  778,  801,  804,  764,  711,  677,  662,  650,  628,  581,
            544,  517,  483,  459,  422,  395,  394,  400,  409,  380,  373,
            352,  279,  186,  111,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
              0,    0,    0,    0,    0,    0,    0,    0], dtype=uint16)

E aqui a figura tosca, mas com os dados passando bem. (Sea Ice, binary data)
    
    
    
    
    ![](http://2.bp.blogspot.com/-T34j3s7kSY0/TzUEmmpLQMI/AAAAAAAAADk/Q1q6BwiFsME/s640/teste2.png)
    
    Figura tosca, mas com os dados funcionando.
    
    
    
    
    
