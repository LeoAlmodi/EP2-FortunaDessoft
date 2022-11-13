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

def valida_questoes(lista):
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
    for i in lista:
        out2.append(valida_questao(i))

    return out2

import random

def sorteia_questao(questao, nivel):
    result =  random.choice(questao[nivel])
    return result

def sorteia_questao_inedita (questao, nivel, lista):
    questao_sort = sorteia_questao(questao, nivel)
    while questao_sort in lista:
        questao_sort = sorteia_questao(questao, nivel)
    lista.append(questao_sort)
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
    return f"DICA:\nOpções certamente erradas: {dicas}"


