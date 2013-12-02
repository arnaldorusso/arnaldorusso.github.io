Title: Ler HDF-EOS de Imagens MODIS com Python
Date: 2012-3-13
Tags: 

Ler HDF de Imagens MODIS com Python.  
Read HDF-EOS with Python  
  
Enfrentei esse problema por um tempo, por conta de como era feito o acesso as variaveis e como elas seriam carregadas.  
Usualmente no laboratorio as pessoas utilizam o "Matlab's" para estas finalidades e para listar os atributos, dao o comando hdfinfo e para carregar o hdfread.  
  
Pelo que li, as bibliotecas incorporadas para essa finalidade, sao desenvolvidas em C. Ja que o HDF-EOS e uma extensao da NCSA (National Center for Supercomputing Applications). Dessa forma, o uso do HDF-EOS (Earth Observing System) e uma das formas cientificas de se guardar os dados hierarquicamente.  
  
Em **Python**, existem algumas bibliotecas para essa finalidade.  
Testei o **gdal**(Geospatial Data Abstraction Library)[1] e o **pyhdf**[2,3]. Ambos sao muito simples de serem instalados.  
  
Antes de mostrar como fazer para carregar os dados, programas no bash shell ja tem uma importante funçao na visualizaçao do HDF. O uso do gdalinfo e habilitado pela intalaçao no proprio linux e o ncdump e uma ferramenta para acesso das informaçoes de NetCDF, mas que funcionou muito bem para o HDF-EOS.  

    
    
    #bash
    # gdalinfo para listar todas os atributos
    yepan@waiapi:$ gdalinfo A20100322010059.L3m_MO_CHL_chlor_a_4km.hdf
    
    #ncdump
    yepan@waiapi:$ ncdump -h A20100322010059.L3m_MO_CHL_chlor_a_4km.hdf
    

Para acesso ao HDF, fiz o seguinte, primeiramente com o gdal.  

    
    
    #!/usr/bin/env python
    
    import gdal
    
    filename = 'A20100322010059.L3m_MO_CHL_chlor_a_4km.hdf'
    ds = gdal.Open(filename)
    sds_md = ds.GetMetadata() #lista os atributos com os valores, guardando
                             #em um dicionario.
    
    for i in sds_md.iterkeys():
        print i,sds_md[i]
    
    data = ds.ReadAsArray()
    data
    Out: 
    array([[-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           ..., 
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.]], dtype=float32)
    
    

Se o HDF tiver algum "Subdataset" e possivel verificar desse jeito:  

    
    
    #!/usr/bin/env python
    
    """
    neste caso e um HDF de coordenadas de gelo
    http://www.iup.uni-bremen.de:8084/amsredata/asi_daygrid_swath/l1a/s6250/grid_coordinates/LongitudeLatitudeGrid-s6250-Antarctic.hdf
    """
    import gdal
    import gdalnumeric
    
    filename = 'LongitudeLatitudeGrid-s6250-Antarctic.hdf'
    
    ds = gdal.Open(filename)
    sds_md = ds.GetMetadata('SUBDATASETS')
    
    {'SUBDATASET_1_DESC': '[1328x1264] Longitudes (32-bit floating-point)',
     'SUBDATASET_1_NAME': 'HDF4_SDS:UNKNOWN:"LongitudeLatitudeGrid-s6250-Antarctic.hdf":0',
     'SUBDATASET_2_DESC': '[1328x1264] Latitudes (32-bit floating-point)',
     'SUBDATASET_2_NAME': 'HDF4_SDS:UNKNOWN:"LongitudeLatitudeGrid-s6250-Antarctic.hdf":1'}
    
    datakeys = {}
    datasets = ['SUBDATASET_1','SUBDATASET_2']
    datanames = ['Longitudes', 'Latitudes']
    
    for (j,i) in enumerate(datasets):
        this = {}
        this['name'] = sds_md[i + '_NAME']
        this['description'] = sds_md[i + '_DESC']
        this['data'] = gdalnumeric.LoadFile(this['name'])
        datakeys[datanames[j]] = this.copy()
    
    #para ver os dados:
    datakeys['Longitudes']['data']
    
    datakeys['Latitudes']['data']
    

Quanto ao pyhdf, nao me aprofundei ainda nos estudos, mas posso adiantar que ele funcionou para abrir a imagem do MODIS e as coordenadas de gelo tambem, mas de forma muito mais simples. Vamos la!  

    
    
    #!/usr/bin/env python
    
    from pyhdf.SD import *
    filename = 'A20100322010059.L3m_MO_CHL_chlor_a_4km.hdf'
    ds = SD(filename)
    ds.attributes() #mostra os atributos
    ds.datasets()
    Out : {'l3m_data': (('fakeDim0', 'fakeDim1'), (4320, 8640), 5, 0)}
    data = ds.select('l3m_data')
    data[:]
    Out :
    array([[-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           ...,
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.],
           [-32767., -32767., -32767., ..., -32767., -32767., -32767.]], dtype=float32)
    

Para acessar as coordenadas de dados de gelo:  

    
    
    #!/usr/bin/env python
    
    from pyhdf.SD import *
    
    filename = 'LongitudeLatitudeGrid-s6250-Antarctic.hdf'
    ds = SD(filename)
    ds.datasets()
    
    Out:  
    {'Latitudes': (('fakeDim2', 'fakeDim3'), (1328, 1264), 5, 1),
     'Longitudes': (('fakeDim0', 'fakeDim1'), (1328, 1264), 5, 0)}
    
    lat = ds.select('Latitudes')
    lat.dimensions()
    Out: {'fakeDim2': 1328, 'fakeDim3': 1264}
    
    #para ver os dados lat[:]
    #Existe tambem a funçao "get", que permite pegar uma porçao do dado, para datasets multidimensionais
    

  
[1] <http://www.gdal.org/>  
[2] <http://hdfeos.org/software/pyhdf.php>  
[3] <http://pysclint.sourceforge.net/pyhdf/>
