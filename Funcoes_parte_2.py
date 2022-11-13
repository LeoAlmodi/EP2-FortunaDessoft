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

