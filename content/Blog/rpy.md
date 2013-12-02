Title: Instalando Rpy
Date: 2013-12-1
Tags: Rpy

Para instalar, você pode fazer o download do pacote 
[Rpy](http://sourceforge.net/projects/rpy/files/).

Lá vocês vão encontrar dois "sabores" de como acessar o seu R pelo python.
Eu prefiro acessar com o *Rpy*, por ser simples e direto.

O Rpy2 é utilizado por default dentro do [Pandas](pandas.pydata.org), mas eu
acho que é tudo muito truncado. Mais pra frente eu posso falar um pouco mais
sobre essa opção.

Descompacte a pasta no seu diretório.

    :::bash
    $ unzip rpy-1.0.3a.zip
    $ cd rpy-1.0.3
    $ python setup.py install

Se você tiver sorte, tudo ocorreu bem...
Caso contrário, algumas modificações terão que ser realizadas.

Para versões mais recentes do R, geralmente o Rpy encontra problemas em
reconhecer o que chamam de "RHOMES", que é onde fica a instalação do seu R.

Existem algumas soluções para isso, descritas no README do pacote.
A que adotei, e pareceu razoável foi a de fazer um link simbólico

    :::bash
    $ sudo ln -s /usr/lib/libR.so /usr/local/lib/
    $ sudo ldconfig

Deverá ocorrer tudo bem agora... mas senão, deve ser por causa do tipo de
bibliotecas que o setup.py está tentando carregar. Geralmente o erro é:

    :::bash
    $ /usr/bin/ld: cannot find -lRlapack

Assim,  deve trocar a linha do setup.py, para carregar a **lapack** ao 
invés de *Rlapack*

    :::vim
    vi setup.py
    :/libraries
    
    # deverá apontar para a linha 163 do código
    libraries = ['R', 'Rlapack']

    # Faça a devida substituição:
    libraries = ['R', 'lapack']

E agora basta instalar!
Espero que tenha dado certo aí também!

Até mais.
