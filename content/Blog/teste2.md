Title: Pelican, a minha mais nova aquisiçao Python 
Date: 2013-11-26
Tags: News, Python
Category: 
Author: 
Summary:

É com grande satisfaçao que volto a escrever no ciclotux.org.

Ainda nao esta 100%, alias nem meu teclado está, mas ao menos nao tenho
que me debater com a plataforma do blogger para poder escrever alguma coisa por aqui.

Era um ponta pé no saco, toda vez ficar logando no bendito sistema, abrir aquela caixinha tosca, pra digitar os codigos em tags html, e a cada preview, ver que o blogger tinha colocado mais um monte de tags que sequer voce tinha criado. Agora chega disso!

O [Pelican](getpelican.com) e´ um gerador de conteudo estatico [obviamente escrito em Python] que atraves de um template e de arquivos em markdown contendo os textos a serem publicados (e onde estou escrevendo esse, agora) gera a saida HTML. Com git, eu empurro tudo isso pro [github](http://github.com), que hospeda esse projeto grauitamente, e assim fica tudo disponibilizado na rede.

Posso garantir, que levei menos tempo pra arrumar esse blog rodando desse jeito, do que organizar 3 codigos que eu quisesse publicar no antigo blogger.

Sem mais delongas por hoje!
Posso dizer que estou feliz!

    :::python
    # Para escrever o post!
    $ vi post_de_hoje.md
    $ git add .
    $ git commit -m 'estreia do Pelican'
    $ git push origin content
        
    # Dentro do diretorio do Blog
    $ make html
    $ make publish
    $ make github

