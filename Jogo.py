import colorama
from colorama import Fore
from colorama import Style
import random

def transforma_base(questoes):
    saida = {}
    for i in questoes:
        n = i['nivel']
        if n not in saida:
            saida[n] = []
        saida[n].append(i)
    return saida

def valida_questao(questao):
    out = {}
    out_op = {}
    dific = ['facil', 'medio' , 'dificil']
    letras = ['A', 'B', 'C', 'D']

    if 'titulo' not in questao.keys():
        out['titulo'] = 'nao_encontrado'
    else:
        if questao['titulo'].strip() == '':
            out['titulo'] = 'vazio'     

    if 'nivel' not in questao.keys():
        out['nivel'] = 'nao_encontrado'
    else:
        if questao['nivel'] not in dific:
            out['nivel'] = 'valor_errado'
    
    if 'opcoes' not in questao.keys():
        out['opcoes'] = 'nao_encontrado'
    else:
        if len(questao['opcoes'].keys()) != 4:
            out['opcoes'] = 'tamanho_invalido'
        else:
            for l, e in questao['opcoes'].items():
                if l in letras:
                    if e.strip() == '':
                        out_op[l] = 'vazia'
                        out['opcoes'] = out_op 
                else:
                    out_op[l] = 'chave_invalida_ou_nao_encontrada'
                    out['opcoes'] = out_op

                
    if 'correta' not in questao.keys():
        out['correta'] = 'nao_encontrado'
    else:
        if questao['correta'] not in letras:
            out['correta'] = 'valor_errado'
    if len(questao.keys()) != 4:
        out['outro'] = 'numero_chaves_invalido'

    return out   

def valida_questoes(questoes):
    def valida_questao(questao):
        out = {}
        out_op = {}
        dific = ['facil', 'medio' , 'dificil']
        letras = ['A', 'B', 'C', 'D']

        if 'titulo' not in questao.keys():
            out['titulo'] = 'nao_encontrado'
        else:
            if questao['titulo'].strip() == '':
                out['titulo'] = 'vazio'     

        if 'nivel' not in questao.keys():
            out['nivel'] = 'nao_encontrado'
        else:
            if questao['nivel'] not in dific:
                out['nivel'] = 'valor_errado'
        
        if 'opcoes' not in questao.keys():
            out['opcoes'] = 'nao_encontrado'
        else:
            if len(questao['opcoes'].keys()) != 4:
                out['opcoes'] = 'tamanho_invalido'
            else:
                for l, e in questao['opcoes'].items():
                    if l in letras:
                        if e.strip() == '':
                            out_op[l] = 'vazia'
                            out['opcoes'] = out_op 
                    else:
                        out_op[l] = 'chave_invalida_ou_nao_encontrada'
                        out['opcoes'] = out_op

                    
        if 'correta' not in questao.keys():
            out['correta'] = 'nao_encontrado'
        else:
            if questao['correta'] not in letras:
                out['correta'] = 'valor_errado'
        if len(questao.keys()) != 4:
            out['outro'] = 'numero_chaves_invalido'

        return out   

    out2 = []
    for i in questoes:
        out2.append(valida_questao(i))

    return out2

def sorteia_questao(questoes, nivel):
    result =  random.choice(questoes[nivel])
    return result

def sorteia_questao_inedita (questoes, nivel, ja_sorteada):
    questao_sort = sorteia_questao(questoes, nivel)
    while questao_sort in ja_sorteada:
        questao_sort = sorteia_questao(questoes, nivel)
    ja_sorteada.append(questao_sort)
    return questao_sort

def questao_para_texto (questao, id):
    return '----------------------------------------\nQUESTAO {}\n\n{}\n\nRESPOSTAS:\nA: {}\nB: {}\nC: {}\nD: {}'.format(id, questao['titulo'], questao['opcoes']['A'], questao['opcoes']['B'], questao['opcoes']['C'], questao['opcoes']['D'])

def gera_ajuda(questao):
    letras = [ "A", "B", "C", "D"]
    letras.remove(questao["correta"])
    i = 1
    ajuda = []
    max = 3
    sorteio = random.randint(1,2)
    sorteio_pergunta = random.randint(1,max-1)
    while sorteio >= i:
        sorteio_pergunta = random.randint(0,max-1)
        if questao["opcoes"][letras[sorteio_pergunta]] not in ajuda:
            ajuda.append(questao["opcoes"][letras[sorteio_pergunta]])
            i += 1
    dicas = " | ".join(ajuda)
    return f"DICA:\nOp????es certamente erradas: {dicas}"


questoes = [{'titulo': 'Qual o resultado da opera????o 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Bras??lia', 'B': 'Rio de janeiro', 'C': 'S??o Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando ?? o feriado da Independ??ncia do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ ?? um conjunto de particularidades que caracterizam um grupo de pessoas, uma fam??lia ou uma sociedade. ?? formada por princ??pios morais, h??bitos, costumes, hist??rias, manifesta????es religiosas, entre outros. Qual palavra melhor completa o in??cio da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miss??o', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culin??ria'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem rela????o com o fen??meno da globaliza????o?',
          'nivel': 'facil',
          'opcoes': {'A': 'Acultura????o', 'B': 'Neoliberalismo', 'C': 'Uni??o Europeia', 'D': 'Caldeir??o do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do anivers??rio da cidade de S??o Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Mar??o', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas n??o ?? uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Ma??a', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilh??o de usu??rios?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes n??o ?? um app com foco em streaming de v??deo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques n??o se localiza em S??o Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas n??o ?? uma linguagem de programa????o?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes ?? menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Nata????o', 'B': 'V??lei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da opera????o 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas ?? uma pseudoci??ncia que estuda os corpos celestes e as prov??veis rela????es que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'F??sica qu??ntica', 'C': 'Astrologia', 'D': 'Computa????o'},
          'correta': 'C'},

         {'titulo': 'Qual destas n??o foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois pr??mios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erd??s', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem ?? considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes n??meros ?? primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um n??mero natural inicial n, onde n > 0, os seguintes crit??rios ser??o obedecidos: Se n for par o seu sucessor ser?? a metade e se n for ??mpar o seu sucessor ser?? o triplo mais um, gerando ent??o um novo n??mero. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincar??', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como fa??o para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodu????o dos seres vivos ?? um processo biol??gico atrav??s do qual os organismos geram descend??ncia. Qual desta n??o ?? uma forma de reprodu????o assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporula????o', 'C': 'Partenog??nese', 'D': 'Divis??o bin??ria'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da opera????o 5 + 2 * 3 ^ 2, onde ^ representa potencia????o?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem ?? Ox??ssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Diss??labo', 'C': 'Divindade das religi??es africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de f??sica em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o n??mero at??mico do nitrog??nio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fus??o do nitrog??nio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120?? C', 'B': '15?? C', 'C': '-210?? C', 'D': '-180?? C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pel?? fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que ?? Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido org??nico'},
          'correta': 'D'}
        ]

colorama.init()

print(f"{Fore.MAGENTA + Style.BRIGHT}Ol??! Voc?? est?? na Fortuna DesSoft e ter?? a oportunidade de enriquecer!{Style.RESET_ALL}")

nome = input('Qual seu nome?')

print(f'\nOk {nome}, voc?? tem direito a pular 3 vezes e 2 ajudas!')
print(f'{Fore.BLUE + Style.BRIGHT}op????es de resposta s??o "A", "B", "C", "D", "ajuda", "pula" e "parar"!{Style.RESET_ALL}\n'  )
input('Aperte ENTER para continuar...')


print('\nO jogo j?? vai come??ar! L?? vem a primeira quest??o!\n\nVamos come??ar com quest??es do n??vel FACIL!\n')  
input('Aperte ENTER para continuar...')


nivel = 'facil'
 
ja_sorteada = []
questao = sorteia_questao_inedita(questoes, nivel, ja_sorteada)