
from game import jogo_da_velha

players = {}

player1 = input('nome do jogador 1:')
symbol1 = input('Jogador 1, escolha X ou O:')
player2 = input('nome do jogador 2:')
if player1 == player2 or player1 == '' or player2 == '':
    print('\nNome inválido para os jogadores:\n')
    
if symbol1 == 'x':
    symbol1 = 'X'
    symbol2 = 'O'
elif symbol1 == 'o' or symbol1 == 'O' or symbol1 == '0':
    symbol1 = 'O'
    symbol2 = 'X'
else:
    print('O simbolo escolhido é desconhecido! O jogador 1 será = X:')
    symbol1 = 'X'
    symbol2 = 'O'
players[player1] = symbol1
players[player2] = symbol2


jogo = jogo_da_velha(players)
jogo.play()

