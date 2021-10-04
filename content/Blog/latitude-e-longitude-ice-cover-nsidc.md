Title: Latitude e Longitude - Ice cover - NSIDC
Date: 2012-12-10
Tags: 

Aproveitando o tempo de recesso sem postagens, vou falar um pouquinho de como fiz para construir as matrizes de lat e long, dos dados de gelo do NSIDC, com as dicas da Claudinha Parise.  
  
Os dados estao em formato binario, como integer e armazenados de 4 em 4 bytes (em Little endian)[1]. Nao sei se o matlab chegaria a dar problemas com isso, mas em Python e bom especificar. ("**<**" Little Endian; "**>**" Big Endian); o "i" e de integer, "u" seria de string(unicode)[2]. Essa foi a dica do Irber; pois eu tava usando dtype = 'uint32', pensando somente na questao dos 4 bytes e esquecendo do "little endian".  
  
Dessa forma, baixa-se o dado de latitude para o hemisferio sul [[aqui](ftp://sidads.colorado.edu/pub/DATASETS/brightness-temperatures/polar-stereo/tools/geo-coord/grid/pss25lats_v3.dat)] e divide-se por 100000 para ter os graus decimais. Mesmo procedimento para a Longitude.  
  

    
    
    import numpy as np
    f = open('pss25lats_v2.dat','rb')
    lat = np.fromfile(f, dtype='<i4')/100000.
    lat = lat.reshape(332,316)
    f.close()
    

  
  
[1] <http://nsidc.org/data/polar_stereo/tools_geo_pixel.html>  
  
[2] <http://docs.scipy.org/doc/numpy/user/basics.byteswapping.html>  
  

