import os
import sys

def banner_inc():
    print("\033[1;91mCyber Security apresenta:\033[0;0m")
    os.system("figlet Aulas")

    print("""
\033[1;34mCRIADOR : Jankees\033[0;0m
    """)

    print("""
\033[1;33m[A]\033[0;0m - \033[1;91mIniciar aula\033[0;0m
\033[1;33m[B]\033[0;0m - \033[1;91mModo de uso\033[0;0m
\033[1;33m[C]\033[0;0m - \033[1;91mSobre a Cyber_Aula\033[0;0m
\033[1;33m[Z]\033[0;0m - \033[1;91mSair\033[0;0m
    """)

    escolha_inicial = input("\033[1;33m[-]\033[0;0m\033[1;34mSua escolha:_> \033[0;0m")

    if escolha_inicial == "a" or escolha_inicial == "A":
        print("\033[1;36mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1")
        main()

    elif escolha_inicial == "b" or escolha_inicial == "B":
        print("\033[1;36mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1")
        print("""
\033[1;36m#MODO DE USO#\033[0;0m
\033[1;32m Para o uso da Cyber_Aulas, se deve inserir os caracteres responsável pelas questões ou escolhas, o uso é simples e descomplicado, então não terão problema de usar a ferramenta!\033[0;0m
        """)
        ret()

    elif escolha_inicial == "c" or escolha_inicial == "C":
        print("\033[1;36mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1")
        print("""
\033[1;32m A Cyber_Aulas foi criada originalmente pela Cyber Security para auxiliar os iniciantes, na resposta de suas duvidas sobre Hacking e Programação!\033[0;0m
        """)
        ret()

    elif escolha_inicial == "z" or escolha_inicial =="Z":
        print("\033[1;36mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1")

        print("\033[1;34mVolte Sempre!\033[0;0m")

def ret():
    return0 = input("\033[1;36mDigite 0 para voltar ao menu de perguntas e 1 para retornar a tela inicial_>  \033[0;0m")
    if return0 == "0" or return0 == "0":
        print("\033[1;36mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        main()
    elif return0 == "1":
        print("\033[1;36mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        banner_inc()
    else:
        os.system("sleep 1")
        print("\033[1;31m[!]\033[0;0m \033[1;34mComando não identificado!\033[0;0m")
        os.system("sleep 1")
        ret()

def main():
    print("""
\033[1;34m[01]\033[0;0m - \033[1;32mAtaques DoS e DDoS diferenças\033[0;0m
\033[1;34m[02]\033[0;0m - \033[1;32mAtaques a Firewall e Servidores\033[0;0m
\033[1;34m[03]\033[0;0m - \033[1;32mProgramação para iniciantes\033[0;0m
\033[1;34m[04]\033[0;0m - \033[1;32mTecnicas de Hacking úteis\033[0;0m
\033[1;34m[05]\033[0;0m - \033[1;32mInvasão a Computadores\033[0;0m 
\033[1;34m[06]\033[0;0m - \033[1;32mTipos de Hackers\033[0;0m
\033[1;34m[07]\033[0;0m - \033[1;32mO que é um Pentest e qual seu objetivo\033[0;0m
\033[1;34m[08]\033[0;0m - \033[1;32mFases de um ataque\033[0;0m
\033[1;34m[09]\033[0;0m - \033[1;32mDefinição de API e de Json\033[0;0m
    """)

    aux = input("\033[1;33m[-]\033[0;0m\033[1;32mSua escolha:_> \033[0;0m")

    if aux == "01" or aux == "1":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("""
\033[1;34mATAQUES DOS E DDOS\033[0;0m
\033[1;32m Basicamente um ataque DoS, da sigla em inglês Denial of Service, é um ataque a um sistema ou servidor ou rede de computadores, que tem como objetivo, torná-lo inacessivel!\033[0;0m

\033[1;32m Já os ataques de rede distribuídos muitas vezes são chamados de ataques de negação de serviço distribuído (DDoS). Esse tipo de ataque aproveita os limites de capacidade específicos que se aplicam a todos os recursos de rede, como a infraestrutura que viabiliza o site de uma empresa. O ataque DDoS envia múltiplas solicitações para o recurso Web invadido com o objetivo de exceder a capacidade que o site tem de lidar com diversas solicitações, impedindo seu funcionamento correto.\033[0;0m
      """)
        ret()

    elif aux == "02" or aux == "2":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("""
\033[1;34mATAQUES A FIREWALL E SERVIDORES\033[0;0m
\033[1;32m Principais métodos de ataques a Firewall e a Servidores são:

\033[1;36m[-]\033[0;0m\033[1;33mAtaques DDoS\033[0;0m
\033[1;32m O DDoS torna uma página indisponível realizando um número enorme de requisições a seu servidor que, por isso, passa a negar as requisições por estar sobrecarregado.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mFoftwares maliciosos (Malwares)\033[0;0m
\033[1;32m Pessoas mal-intencionadas desenvolvem softwares maliciosos, como cavalos de troia, vírus e outros, com objetivo de infectar o alvo e causar danos aos seus servidores. Esses programas normalmente são distribuídos através de e-mail, escondidos em aplicações que são de interesse dos usuários ou, ainda, explorando brechas de segurança que permitem a implantação do código malicioso.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mAtaques de Força Bruta (Brute Force)\033[0;0m
\033[1;32m Esse tipo de ataque é utilizado para quebrar senhas através da tentativa de todas as combinações possíveis. Trata-se de um software que testa automaticamente milhões de combinações de senha até encontrar a correta e, então, invadir o servidor.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mPort Scanning Attack\033[0;0m
\033[1;32m  Quando um hacker envia requisições para diversas portas do servidor procurando alguma brecha que permita uma invasão, ele está realizando um Port Scanning Attack. Normalmente, é feita de forma automatizada por algum software para ganhar tempo e, dependendo da resposta que a porta dá para a requisição enviada, o hacker avalia se é viável ou não utilizá-la para um ataque.\033[0;0m
        """)
        ret()

    elif aux == "03" or aux == "3":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("\033[1;34mPROGRAMAÇÃO PARA INICIANTES\033[0;0m")
        print("""
\033[1;32mAs principais linguagens de programação para iniciantes, são:\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mGo\033[0;0m
\033[1;32m Go é uma das linguagens de programação mais modernas e populares atualmente. Go é gerenciada e mantida pelo Google. Em alguns aspectos, Go é ainda melhor em comparação com Python.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mJavaScript\033[0;0m
\033[1;32m JavaScript é a linguagem onipresente na web. Não é usada apenas no front-end, mas também no back-end. Atualmente, JavaScript é muito usada (e cada vez mais) em Machine Learning, Desenvolvimento Web e Desenvolvimento de Jogos.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mC e C++\033[0;0m
\033[1;32m C e C ++ é a primeira linguagem de programação que geralmente aprendemos em nossos dias no curso de graduação em Ciência da Computação. Se você está iniciando em Programação e deseja criar uma base sólida em Programação e Ciência da Computação, definitivamente deve usar C / C ++.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mPython\033[0;0m
\033[1;32m Python é uma linguagem de programação multiuso, mas que vem sendo usada principalmente para desenvolvimento web e análise de dados. É uma das linguagens de programação mais fáceis para quem está começando em programação.\033[0;0m
        """)
        ret()

    elif aux == "4" or aux == "04":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("""
\033[1;32mTÉCNICAS DE HACKING ÚTEIS\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mMetasploit\033[0;0m
\033[1;32m Metasploit é um projeto de segurança de informação que divulga informações relacionadas a vulnerabilidades e busca facilitar testes de penetração e o desenvolvimento de Sistema de detecção de intrusos.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mBurpSuite\033[0;0m
\033[1;32m Burp Suite é um software desenvolvido em Java pela PortSwigger, para a realização de testes de segurança em aplicações web. O Burp Suite é dividido em diversos componentes.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mNMap\033[0;0m
\033[1;32mO Nmap é um programa que permite fazer um scan completo em uma rede, para se obter as informações de quais hosts estão nela ativos. Além disso, ele também permite fazer scan de porta, a fim de descobrir quais portas estão abertas, assim como fornece a informação de quais sistemas estão rodando em um dado momento.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mAirCrack-ng\033[0;0m
\033[1;32m Aircrack-ng é um detector de redes, sniffer de pacote, aplicativo de quebra de WEP e ferramenta de análise para redes locais sem fios 802.11. Funciona com qualquer placa wireless cujo driver suporta modo de monitoramento bruto e pode capturar e analisar tráfego 802.11a, 802.11b e 802.11g.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mHashCat\033[0;0m
\033[1;32m O Hashcat é uma poderosa ferramenta de força bruta de passwords e hashs e é muito utilizada devido a sua performance e eficiência. ... No exemplo ele identificou a hash como uma possível MD5. Salve todas as hashs num txt chamado hash.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mJonh-the-Ripper\033[0;0m
\033[1;32m John the Ripper é um software para quebra de senhas. Inicialmente desenvolvido para sistemas unix-like, corre agora em vários sistemas operativos. Disponível em versão gratuita e paga, o John the Ripper é capaz fazer força bruta em senhas cifradas em DES, MD4 e MD5 entre outras.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mCobalt-Strike\033[0;0m
\033[1;32m Cobalt Strike é uma ferramenta usada para detectar vulnerabilidades de penetração no sistema. A ferramenta em si deve ser usada para teste de software, a fim de encontrar vários erros e falhas. No entanto, o problema é que os criminosos geralmente aproveitam-se de tais ferramentas e Cobalt Strike não é uma exceção.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mOwasp-Zap\033[0;0m
\033[1;32m Automatizando testes de vulnerabilidades em aplicações web com o OWASP ZAP e Python. Fundada em 2001, a OWASP (Open Web Application Security Project) é uma comunidade online que cria e disponibiliza de forma gratuita artigos, metodologias, documentação, ferramentas e tecnologias no campo da segurança de aplicações.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mSqlMap\033[0;0m
\033[1;32m Sqlmap é uma ferramenta open source para teste de penetração que automatiza o processo de detecção e exploração de vulnerabilidades de Injeção de SQL, permitindo a invasão de banco de dados de sites.\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33mCommix\033[0;0m
\033[1;32m Ferramenta automatizada de injeção e exploração de comandos do sistema operacional, tudo em um.\033[0;0m

        """)
        ret()

    elif aux == "05" or aux == "5":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("""
\033[1;32INVASÃO A COMPUTADORES\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;32m O objetivo de muitos criadores de vírus de computador e criminosos virtuais é distribuir seus vírus, worms ou cavalos de Troia para o maior número possível de computadores ou celulares, maximizando a abrangência de seus programas de malware. Existem três maneiras principais como isso pode ser feito:\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;32mPor engenharia social\033[0;0m
\033[1;36m[-]\033[0;0m \033[1;32mInfectando um sistema sem conhecimento do usuário\033[0;0m
\033[1;36m[-]\033[0;0m \033[1;32mCombinando esses dois métodos\033[0;0m

\033[1;32m Além disso, muitas vezes o criador do malware ainda toma medidas para impedir que a infecção seja detectada por programas antivírus.\033[0;0m
        """)
        ret()

    elif aux == "06" or aux == "6":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("""
\033[1;34mTIPOS DE HACKERS\033[0;0m

\033[1;36m[-]\033[0;0m\033[1;33m White Hat Hackers\033[0;0m

\033[1;32m Os White Hat Hackers também são conhecidos por hackers de chapéu branco ou hackers éticos.
Eles trabalham junto com organizações com o objetivo de fortalecer a segurança de seus sistemas. Os white hat hackers podem invadir e comprometer sistemas através de meios legais, para então informar a empresa sobre todas as vulnerabilidades e brechas de segurança que encontraram nos sistemas. Este tipo de hacker domina técnicas, metodologias e ferramentas do chamado hacking ético.
\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mBlack Hat Hackers\033[0;0m

\033[1;32m Conhecidos mais comumente como crackers, os hackers de chapéu preto são aqueles que invadem uma rede ou sistema sem autorização para explorá-los com objetivos maliciosos e em benefício próprio. Dentro desta categoria se encontram os cibercriminosos.\033[0;0m
\033[1;32m O foco dos Black Hat Hackers é infligir danos a sites, sistemas e redes para obter acesso a dados pessoais que podem ser usados para golpes, fraudes e outros crimes.
Esses hackers utilizam meios ilegais para seus ataques, mas frequentemente exploram falhas humanas para realizá-los.\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mGray Hat Hackers\033[0;0m
\033[1;32m Os Gray Hat Hackers são o meio termo entre os hackers. Eles exploram sistemas e redes sem autorização, no entanto não o fazem para benefícios próprios, mas sim para alertar empresas e agências de segurança sobre as vulnerabilidades e brechas de segurança que possuem, tal como fazem os pentesters.\033[0;0m
        """)
        ret()

    elif aux == "07" or aux == "7":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("""
\033[1;34mO QUE É UM PENTEST E QUAL SEU OBJETIVO\033[0;0m

\033[1;32m O Pentest é uma forma de detectar e explorar vulnerabilidades existentes nos sistemas, ou seja, simular ataques de hackers. Essas avaliações são úteis para validar a eficácia dos mecanismos de defesa do aplicativo e dos servidores por trás dele.\033[0;0m
        """)
        ret()

    elif aux == "08" or aux == "8":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")
        print("""
\033[1;34mFASES DE UM ATAQUE\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mColeta de informações.\033[0;0m

\033[1;32m Os agentes criminosos identificam e coletam informações disponíveis publicamente sobre seus alvos para personalizar seus ataques. Essa fase inicial visa obter informações estratégicas, não apenas sobre o ambiente de TI do alvo pretendido, mas também sobre sua estrutura organizacional. As informações coletadas podem variar desde aplicativos de negócios e software que uma empresa utiliza até sobre as funções e relacionamentos que existem no ambiente interno. Essa fase também utiliza técnicas de engenharia social, que avaliam eventos recentes, questões ou preocupações relacionadas ao trabalho e outras áreas de interesse para o alvo pretendido.\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mPonto de entrada.\033[0;0m

\033[1;32m Os hackers podem usar métodos variados para se infiltrar na infraestrutura de um alvo. Os métodos mais comuns incluem e-mail personalizado de spear phishing, exploits de dia zero ou de software e técnicas de watering hole. Os atacantes também utilizam plataformas de mensagens instantâneas e redes sociais para induzir alvos a clicar em um link ou baixar malware. Eventualmente, conseguem estabelecer uma conexão com o alvo.\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mComunicação de comando e controle (C&C).\033[0;0m

\033[1;32m Depois que a segurança foi violada, os agentes de ameaças se comunicam constantemente com o malware, para executar rotinas maliciosas ou coletar informações dentro da rede da empresa. Os atores maliciosos usam técnicas para esconder essa comunicação e manter seus movimentos sob controle.\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mMovimento lateral.\033[0;0m

\033[1;32m Uma vez dentro da rede, os agentes de ameaças se movem lateralmente pela rede para buscar informações importantes ou infectar outros sistemas valiosos.\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mDescoberta de ativos ou dados.\033[0;0m

\033[1;32m Ativos ou dados valiosos são identificados e isolados para futura extração de dados. Os agentes de ameaças têm acesso a “territórios” que contêm informações e ativos valiosos. Esses dados são então identificados e transferidos por meio de ferramentas como RATs (Trojans de Acesso Remoto) e ferramentas personalizadas e legítimas. Uma técnica possível usada neste estágio pode ser o envio de listas de arquivos em diretórios diferentes para que os invasores possam identificar o que é valioso.\033[0;0m


\033[1;36m[-]\033[0;0m \033[1;33mExfiltração de Dados.\033[0;0m

\033[1;32m Esse é o objetivo principal dos ataques direcionados. O objetivo de um ataque sempre é coletar informações importantes e transferi-las para um local controlado pelos invasores. A transferência desses dados pode ser realizada de forma rápida ou gradual. Os ataques direcionados se esforçam para não serem detectados na rede, a fim de obter acesso às joias da coroa ou a dados empresariais que possam ter algum valor. Esses dados valiosos incluem propriedade intelectual, segredos comerciais e informações de clientes. Além disso, os agentes de ameaças também podem buscar outros dados confidenciais, como documentos ultrassecretos de instituições governamentais ou militares.\033[0;0m
        """)
        ret()

    elif aux == "09" or aux == "9":
        print("\033[1;32mAguarde! Estou processando...\033[0;0m")
        os.system("sleep 1 && clear")

        print("""
\033[1;34mDEFINIÇÃO DE API E JSON\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mAPI\033[0;0m

\033[1;32m API é um acrônimo em inglês que significa interface de programação de aplicações. Uma API permite que sua solução ou serviço se comunique com outros produtos e serviços sem precisar saber como eles foram implementados.\033[0;0m

\033[1;36m[-]\033[0;0m \033[1;33mJSON\033[0;0m

\033[1;32m Em computação, JSON, um acrônimo de JavaScript Object Notation, é um formato compacto, de padrão aberto independente, de troca de dados simples e rápida entre sistemas, especificado por Douglas Crockford em 2000, que utiliza texto legível a humanos, no formato atributo-valor.\033[0;0m
        """)
        ret()

banner_inc()
