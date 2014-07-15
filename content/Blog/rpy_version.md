Title: Instalando Rpy - Diferentes versões de R
Date: 2014-4-14
Tags: Rpy

Para instalar o **rpy** é necessário ter o R instalado em uma versão menor
que a "3". Para tanto é necessário que se faça o download da versão desejada e a
compile com especial atenção

    :::bash
    $ cd ~
    $ wget -c http://cran.r-project.org/src/base/R-2/R-2.15.1.tar.gz
    $ tar -xzv R-2.15.1.tar.gz
    $ cd R-2.15.1
    $ ./configure --enable-R-shlib # Isto é indicação do **rpy**
    $ make

Depois disso é necessário instalar o rpy, que tem alguns poréns.
O primeiro deles é ao identificar qual a versão do R que se deve utilizar.
Baixe o arquivo [aqui](http://sourceforge.net/projects/rpy/files/rpy/1.0.3/rpy-1.0.3.tar.gz/download)

    :::bash
    $ export RHOMES=$HOME/R-2.15.1
    
    Ou inserir diretamente a linha no seu .bashrc

    $ vim ~/.bashrc
    export RHOME=~/R-2.15.1
    

A segunda etapa é modificar o arquivo setup.py, de acordo com a postagem
[Instalando Rpy](http://ciclotux.org/instalando-rpy.html), substituindo a 
biblioteca 'Rlapack' por 'lapack'.

O terceiro passo, o qual gerou tanta dor de cabeça, é o fato do **Rpy** manter
um erro de REGEX no seu código.

Para isso é necessário modificar a sentença:

    :::bash
    $ tar -xzv rpy-1.0.3.tar.gz
    $ cd rpy-1.0.3
    $ vim rpy_tools.py
    
    Na linha 101 a regex está incompleta:
    version = re.search(" +([0-9]\.[0-9]\.[0-9])", output)

    Modifique para:
    version = re.search(" +([0-9]\.[0-9]+\.[0-9])", output)

Após isso falta pouco!
É necessário alterar o arquivo src/RPY.h

    :::bash
    $ cd rpy-1.0.3/src
    $ vim RPy.h

    Na linha que diz:
    #include <Rdevices.h> /* must follow Graphics.h */
    
    Modifique para:
    #include <Rembedded.h> /* must follow Graphics.h */

Depois disso tudo:

    :::bash
    $ python setup.py install

Enquanto não consigo migrar os meus códigos de rpy, para rpy2, vou quebrando
a cabeça para fazer o rpy funcionar.
Obrigado novamente ao Jedi Irber, que ajudou a solucionar o problema. =]

Até mais.
