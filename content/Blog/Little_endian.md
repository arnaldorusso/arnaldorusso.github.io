Title: One Little two, little three, little Endian 
Date: 2014-11-25
Tags: Python, dtype 

Sempre que me deparo com os amigos bytes empilhados, recorro ao oráculo
tentando entender como são feitas as codificações dessas coisas, para
algo que possamos entender.

Para abrir os dados de gelo marinho, em uma das plataformas de dados é a codificação "flat binary two-byte integer" [dados Nimbus 7](http://nsidc.org/data/docs/daac/nsidc0079_bootstrap_seaice.gd.html).

Para abrir esse dado:

    :::python
    import numpy as np
    f = open('name_of_file','rb')
    SeaIce = np.fromfile(f, dtype=np.uint16).reshape(332, 316)

Apesar dos dados estarem como two-byte integer, os dados de georeferência estão
em outra codificação [Pode ser baixado
aqui](ftp://sidads.colorado.edu/pub/DATASETS/seaice/polar-stereo/tools/) e a
codificação e explicações estão
[aqui](http://nsidc.org/data/polar_stereo/tools_geo_pixel.html#dataviewer.sav).

As orientações são:

    Grids that determine the longitude of a given pixel for the 25 km grids
    for either hemisphere (psn for the Northern Hemisphere and pss for the
    Southern Hemisphere). These longitude grids are in binary format and are
    stored as 4-byte integers (little endian) scaled by 100,000 (divide the
    stored value by 100,000 to get decimal degrees). Each array location 
    (i, j) contains the longitude value at the center of the corresponding 
    data grid cells. An East-longitude convention is used; therefore, 
    positive longitude values are to the east of Greenwich, England.

    psn25lons_v3.dat: 304 columns x 448 rows, range = [-180.000, 179.814]
    pss25lons_v3.dat: 316 columns x 332 rows, range = [-179.818, 179.818]

Para isso o simples código resolve:

    :::python
    import numpy as np

    f = open('pss25lons_v3.dat', 'rb')
    raw_lons = np.fromfile(f, dtype='<i4') # 4-byte integers (little endian)
    lons = raw_lons.reshape(332,316) / 100000.

    In [101]: lons
    Out[101]: 
    array([[ -42.23257,  -42.05101,  -41.8684 , ...,   41.8684 ,   42.05101,
              42.23257],
           [ -42.39744,  -42.21577,  -42.03306, ...,   42.03306,   42.21577,
              42.39744],
           [ -42.56335,  -42.38159,  -42.19877, ...,   42.19877,   42.38159,
              42.56335],
           ..., 
           [-134.6339 , -134.81636, -135.     , ...,  135.     ,  134.81636,
             134.6339 ],
           [-134.81753, -135.     , -135.18364, ...,  135.18364,  135.     ,
             134.81753],
           [-135.     , -135.18247, -135.3661 , ...,  135.3661 ,  135.18247,
             135.     ]])
