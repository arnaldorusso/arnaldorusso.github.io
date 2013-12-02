Title: Subset MODIS-Aqua (Clorofila-a)
Date: 2012-4-28
Tags: MODIS scipy matplotlib python Remote Sensing numpy Aqua

Pegando o gancho com uma postagem [[1]](http://www.trondkristiansen.com/?page_id=479) que ja tinha guardada de um tempo e do pacote pyMODIS [[2]](https://bitbucket.org/tylere/pymodis/overview), resolvi fazer o meu subset de imagens MODIS em Python.  
  
Para esse codigo, foram testadas apenas imagens L3 de Clorofila-a, ja processadas pela agencia espacial norte americana (NASA).  
  
Para executar esse codigo, voce precisara de uma imagem: [Imagem MODIS de 9km.](http://oceandata.sci.gsfc.nasa.gov/cgi/getfile/A20120012012031.L3m_MO_CHL_chlor_a_9km.bz2)  
  
De um bunzip2 no seu diretorio, onde estao as imagens .bz2, para que o codigo abaixo identifique somente as imagens sem a extensao (.bz2).  
  
Um detalhe, e que abaixo segue como fazer o processo em batelada, mas para o exemplo de uma imagem, ja e possivel visualizar a coisa.   
  
Diferentemente do post [[1]](http://www.trondkristiansen.com/?page_id=479), nao encontrei dificuldades em utilizar os dados. Logo nao fiz uma conversao em ascii e nem utilizei o HDFview.  
  
[1] <http://www.trondkristiansen.com/?page_id=479>  
[2] <https://bitbucket.org/tylere/pymodis/overview>  
  

    
    
    #/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    '''
    subset_MODIS
    
    Programa para Fazer um subset de imagens MODIS
    Dentro dos limites Lat e Long determinados.
    
    Author =  Arnaldo Russo
    e-mail =  arnaldorusso@gmail.com
    '''
    from pyhdf.SD import *
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.io
    import glob
    
    #setting limits to be cut
    LATLIMS = ([-40, -30])
    LONLIMS = ([-40, -30])
    
    indir = '/DATA/database/Images/L3/9km/'
    outdir = '/DATA/database/Images/L3/resize/'
    
    filelist = glob.glob(indir+'A*')
    nfiles = len(filelist)
    files = []
    for path in filelist:
      files.append(path[len(indir):]) #remove path name
    
    names = []
    multi_img = []
    for i in range(len(filelist)):
        A = SD(filelist[i])
        a = A.attributes()
        for k in xrange(0,len(a.keys())):
            nm = a.keys()[k]
            names.append(nm.replace(" ","_"))
        pin = dict(zip(names,a.values()[:]))
        lon = np.arange(pin['Westernmost_Longitude'],pin['Easternmost_Longitude'],pin['Longitude_Step'])
        lat= np.arange(pin['Northernmost_Latitude'],pin['Southernmost_Latitude'],-pin['Latitude_Step'])
        #Get the indices needed for the area of interest
        ilt = np.int(np.argmin(np.abs(lat-max(LATLIMS)))) #argmin catch the indices
        ilg = np.int(np.argmin(np.abs(lon-min(LONLIMS)))) #of minor element
        ltlm = np.int(np.fix(np.diff(LATLIMS)/pin['Latitude_Step']+0.5))
        lglm = np.int(np.fix(np.diff(LONLIMS)/pin['Longitude_Step']+0.5))
        #retrieve data SDS
        d = A.datasets()
        sds_name = d.keys()[0] #name of sds. Dictionary method.
        sds = A.select(sds_name)
        #load the subset of data needed for the map limits given
        P = sds[ilt:(ilt+ltlm),ilg:(ilg+lglm)]
        P[P==-32767]=np.nan #Rrs_670:bad_value_scaled = -32767s ;
        P=np.double(P)
        P=(pin['Slope']*P+pin['Intercept'])
        LT=lat[ilt+np.arange(0,ltlm-1)]
        LG=lon[ilg+np.arange(0,lglm-1)]
        Plg,Plt = np.meshgrid(LG,LT) #Further plots
        P = np.log(P) #chlorophyll mapping
        multi_img.append(P)
    
    
    multi_img = np.asarray(multi_img)
    plt.imshow(P)
    plt.show()
    
    ### Save matrix
    np.save("multi_img",multi_img)
    # If you want to share with your Matlab friends Users =]
    scipy.io.savemat(outdir+'multi_matrix.mat', mdict={'multi_img': multi_img})
    
    

  
Resultando nessa imagem de Clorofila-a  


![](http://2.bp.blogspot.com/-mDQntMCRnWU/T5vXVhAO9BI/AAAAAAAAAKc/2SK7jkOqJKw/s320/chla.png)

  

