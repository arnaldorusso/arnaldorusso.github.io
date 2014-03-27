Title: Impressão no seu servidor remoto
Date: 2014-03-27
Tags:

Ontem me senti super feliz ao conseguir conversar com a impressora através de 
um simples **lpr**.

Obviamente a linha de texto faz tudo que a sua interface gráfica deixa disponibilizado para você,
mas é sempre muito bom quando se consegue algo que sua interface não deixou ali pra você. 
Digo isso no caso em que sua outra máquina é um servidor e que a tela é sim, somente uma tela
preta.

Antes de enviar o arquivo para o seu servidor, preste atenção com o **scp** pois 
de alguma maneira o flag de porta não é o mesmo que para ssh **-p** e sim **P** Maiúsculo.

    :::bash
    scp -P Num_da_porta /local/do/seu/arquivo.pdf user@server_IP:local/para/onde/enviar

Após isso, na sua sessão logada no server, descubra qual a impressora que você deseja imprimir.
Geralmente existe a impressora padrão do sistema, mas você pode escolher para qual direcionar.

    :::bash
    ssh -p Num_da_porta user@server_IP
    lpstat -p -d

Isso retornará uma lista das impressoras em sua rede e plugadas localmente.

Depois disso, basta  mandar imprimir da sua casa, na impressora do seu servidor.
    
    :::bash
    lpr -P nome_da_impressora NomeDoArquivo.pdf



