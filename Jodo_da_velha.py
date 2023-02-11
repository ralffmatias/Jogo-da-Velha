tb1 = [['_', '_', '_'], ['_', '_', '_'], [' ', ' ', ' ']]
players = {}
names = []
winner = ''
score = {}
result = ''


# Cria os jogadores atribuindo o simbolo ao nome no dicionário:
def criarjogadores():
    player1 = input('nome do jogador 1:')
    symbol1 = input('Jogador 1, escolha X ou O:')
    player2 = input('nome do jogador 2:')
    if player1 == player2 or player1 == '' or player2 == '':
        print('\nNome inválido para os jogadores:\n')
        return criarjogadores()
    if symbol1 == 'x':
        symbol1 = 'X'
        symbol2 = 'O'
    elif symbol1 == 'o' or symbol1 == 'O' or symbol1 == 0:
        symbol1 = 'O'
        symbol2 = 'X'
    else:
        print('O simbolo escolhido é desconhecido! O jogador 1 será = X:')
        symbol1 = 'X'
        symbol2 = 'O'
    players[player1] = symbol1
    players[player2] = symbol2
    score[player1] = 0
    score[player2] = 0
    for j in players.keys():
        names.append(j)
    return players, names, score


# Imprimir board:
def board(tb):
    jog1 = names[0]
    jog2 = names[1]
    print('           score(' + jog1 + ':' + str(score[jog1]) + '|' + jog2 + ':' + str(score[jog2]) + ')\n     a  b  c')
    for c in range(0, 3):
        print('    ' + str(c + 1) + ' ' + str(tb[c][0]) + '|' + str(tb[c][1]) + '|' + str(tb[c][2]))
    print('_____________________\n       digite "exit" para encerrar!\n')


# funções auxiliares de jogada
# vitória:
def vitoria(invertname, tb):
    for j in invertname:
        s = players[j]
        retorno = 'congratulations ' + j + ': you win!'
        if tb[0][0] == s and tb[0][1] == s and tb[0][2] == s:
            print(retorno)
            return j
        elif tb[1][0] == s and tb[1][1] == s and tb[1][2] == s:
            print(retorno)
            return j
        elif tb[2][0] == s and tb[2][1] == s and tb[2][2] == s:
            print(retorno)
            return j
        elif tb[0][0] == s and tb[1][0] == s and tb[2][0] == s:
            print(retorno)
            return j
        elif tb[0][1] == s and tb[1][1] == s and tb[2][1] == s:
            print(retorno)
            return j
        elif tb[0][2] == s and tb[1][2] == s and tb[2][2] == s:
            print(retorno)
            return j
        elif tb[0][0] == s and tb[1][1] == s and tb[2][2] == s:
            print(retorno)
            return j
        elif tb[2][0] == s and tb[1][1] == s and tb[0][2] == s:
            print(retorno)
            return j
    return 0


# Quando o tabuleiro encher:
def boardnotfull(tb):
    for n in range(0, 3):
        for j in range(0, 3):
            if tb[j][n] == ' ' or tb[j][n] == '_':
                return True


# Inverte a coluna em índice:
def colunaletra(c):
    if c == 'a':
        c = 0
    elif c == 'b':
        c = 1
    elif c == 'c':
        c = 2
    return c


# verifica as variaveis de linha e coluna:
def checkmove(line, column, j, tb):
    if column != 'a' and column != 'b' and column != 'c' or line != '1' and line != '2' and line != '3':
        print('\nValor desconhecido: tente de novo!\n')
        column = input(j + ' escolha a coluna: a, b ou c:')
        line = input('agora escolha a linha: 1, 2 ou 3:')
        return checkmove(line, column, j, tb)
    else:
        column = colunaletra(column)
        line = int(line)
        line -= 1
        if tb[line][column] == 'X' or tb[line][column] == 'O':
            print('\nesse bloco ja está ocupado tente novamente:\n')
            column = input(' escolha a coluna: a, b ou c:')
            line = input('agora escolha a linha: 1, 2 ou 3:')
            return checkmove(line, column, j, tb)
        return line, column


# função jogar:
def jogada(invertname, tb):
    for j in invertname:
        notwin = vitoria(invertname, tb)
        if notwin == 0:
            if boardnotfull(tb):
                column = input(j + ' escolha a coluna: a, b ou c:')
                if column == 'exit':
                    return column
                line = input('agora escolha a linha: 1, 2 ou 3:')
                if line == 'exit':
                    return line
                line, column = checkmove(line, column, j, tb)
                tb[line][column] = players[j]
                board(tb)
                if j == invertname[1]:
                    return jogada(invertname, tb)
            else:
                print('      DEU VELHA #:')
                return 0
        else:
            return notwin


# score
def pscore(result):
    j1 = names[0]
    j2 = names[1]
    if result == j1:
        score[j1] += 1
        return score
    elif result == j2:
        score[j2] += 1
        return score
    return score


# função inverter jogada
def invert(result):
    if result == names[1]:
        invertname = [names[1], names[0]]
        return invertname
    return names


# chamar funções de jogo:
def play(result, tb):
    criarjogadores()
    for i in range(0, 5):
        if result != 'exit':
            tb = [['_', '_', '_'], ['_', '_', '_'], [' ', ' ', ' ']]
            score = pscore(result)
            invertname = invert(result)
            print('\n****new game****')
            board(tb)
            result = jogada(invertname, tb)
    if score[names[0]] == score[names[1]]:
        print('game encerrado:\n   sem ganhadores')
    else:
        print('game encerrado:\n     ' + max(score, key=score.get) + ' é o vencedor!')


play(result, tb1)
