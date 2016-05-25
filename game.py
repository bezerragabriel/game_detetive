jogador = input("Nome de usuário: ")

op = input("Digite 'I' para instruções e 'J' para iniciar o jogo: ")

if (op == "I"):

    print ("Ao iniciar o jogo, serão disponibilizadas 9 cartas (3 cartas correspondentes aos suspeitos, 3 correspondentes as armas e 3 correspondentes as cenas do crime) porém sem que seja revelado o seu conteúdo. O jogador deverá escolher 1 carta de cada categoria e a combinação que o jogador escolher determinará as características do crime. No decorrer do jogo, o jogador receberá dicas que o ajudarão a responder questões que, se respondidas corretamente, o levarão à solucionar o incrível mistério!")

print ("Seja bem-vindo(a),", jogador, "!")

local = ["Quarto", "Cozinha", "Escritório", "Banheiro", "Beco", "Salão de festas", "Floresta", "Carro", "Escola"]
objeto = ["Revólver", "Tesoura", "Punhal", "Veneno", "Corda", "Machado"]
pessoa = ["Arnold Clark", "Patricia Devon", "James Miller", "Sharon Stone", "Marcos Schneider", "Eduarda Richkovsky"]

import random  # Importamos a função Random, que seleciona números aleatórios como num sorteio

sort_1 = random.sample(range(0,9),3)  # Sorteamos 3 números (cartas) de 1 a 9 na categoria de Cenas do Crime 
sort_2 = random.sample(range(0,6),3)  # Aqui, sorteamos 3 números na categoria Armas
sort_3 = random.sample(range(0,6),3)  # Aqui, foram sorteados 3 na categoria Suspeitos

for i in range(3):  # Aqui, usamos o For para armazenar os números sorteados em vetores

    sort_1[i] = local[sort_1[i]]
    sort_2[i] = objeto[sort_2[i]]
    sort_3[i] = pessoa[sort_3[i]]

crime = []

for i in range(3): # O jogador deve, agora, selecionar os numeros que foram guardados nos vetores

    x = int(input("Escolha um número entre 0 e 2:"))
    crime.append(x)

crime[0] = sort_1[crime[0]]
crime[1] = sort_2[crime[1]]
crime[2] = sort_3[crime[2]]
