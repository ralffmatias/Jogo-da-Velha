import os

class jogo_da_velha:
    
    # Mensagens de print:
    __msg = {
                'unknown_value' : '\nValor desconhecido: tente de novo!\n',
                'block_occupied': '\nEsse bloco já está ocupado, tente novamente:\n',
                'game_draw'     : '      DEU VELHA #:',
                'player_win'    : 'Congratulations %s: you win!',
                'no_winner'     : '   Sem ganhadores',
                'winner'        : 'Game encerrado:\n     %s é o vencedor!',
                'imput_line'    : 'Agora escolha a linha: 1, 2 ou 3:',
                'imput_column'  : '%s, escolha a coluna: A, B ou C:'
            }

    # Cria os jogadores atribuindo o simbolo ao nome no dicionário:
    def __init__(self, players):
        self.players = players
        self.score = {player: 0 for player in players} 
        self.names = list(players.keys())
        self.__tb = []


    # Imprimir board:
    def __board(self):
        jog1 = self.names[0]
        jog2 = self.names[1]
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n****new game****')
        print('           score(%s:%d|%s:%d)\n     a  b  c' % (jog1, self.score[jog1], jog2, self.score[jog2]))
        for c in range(0, 3):
            print('    %d %s|%s|%s' %(c + 1, self.__tb[c][0], self.__tb[c][1], self.__tb[c][2]))
        print('_____________________\n       digite "exit" para encerrar!\n')


    # funções auxiliares de __jogada...
    # vitória:
    def __vitoria(self, invertname):
        for j in invertname:
            s = self.players[j]
            if (
                        (self.__tb[0][0] == s and self.__tb[0][1] == s and self.__tb[0][2] == s) 
                    or  (self.__tb[1][0] == s and self.__tb[1][1] == s and self.__tb[1][2] == s)
                    or  (self.__tb[2][0] == s and self.__tb[2][1] == s and self.__tb[2][2] == s)
                    or  (self.__tb[0][0] == s and self.__tb[1][0] == s and self.__tb[2][0] == s)
                    or  (self.__tb[0][1] == s and self.__tb[1][1] == s and self.__tb[2][1] == s)
                    or  (self.__tb[0][2] == s and self.__tb[1][2] == s and self.__tb[2][2] == s)
                    or  (self.__tb[0][0] == s and self.__tb[1][1] == s and self.__tb[2][2] == s)
                    or  (self.__tb[2][0] == s and self.__tb[1][1] == s and self.__tb[0][2] == s)
                ):
                return j
        return 0


    # Quando o tabuleiro encher:
    def __boardnotfull(self):
        return any(cell in [' ', '_'] for row in self.__tb for cell in row)


    # Inverte a coluna em índice:
    def __colunaletra(self, c):
        map = {'a': 0, 'b': 1, 'c': 2}
        return map[c]


    # verifica as variaveis de linha e coluna:
    def __checkmove(self, line, column, imput_column):
        if column != 'a' and column != 'b' and column != 'c' or line != '1' and line != '2' and line != '3':
            print(self.__msg['unknown_value'])
            column = input(imput_column)
            line = input(self.__msg['imput_line'])
            return self.__checkmove(line, column, imput_column)
        else:
            column = self.__colunaletra(column)
            line = int(line) - 1
            if self.__tb[line][column] in ['X', 'O']:
                print(self.__msg['block_occupied'])
                column = input(imput_column)
                line = input(self.__msg['imput_line'])
                return self.__checkmove(line, column, imput_column)
            return line, column


    # função jogar:
    def __jogada(self, invertname):
        for j in invertname:
            imput_column = self.__msg['imput_column'] % j
            notwin = self.__vitoria(invertname)
            if notwin == 0:
                if self.__boardnotfull():
                    column = input(imput_column)
                    if column == 'exit':
                        return column
                    line = input(self.__msg['imput_line'])
                    if line == 'exit':
                        return line
                    line, column = self.__checkmove(line, column, imput_column)
                    self.__tb[line][column] = self.players[j]
                    self.__board()
                    if j == invertname[1]:
                        return self.__jogada(invertname)
                else:
                    print(self.__msg['game_draw'])
                    return 0
            else:
                print(self.__msg['player_win'] % notwin)
                return notwin


    # score:
    def __pscore(self, result):
        j1 = self.names[0]
        j2 = self.names[1]
        if result == j1:
            self.score[j1] += 1
            return self.score
        elif result == j2:
            self.score[j2] += 1
            return self.score
        return self.score


    # função para inverter ordem de jogada (O ultimo vencedor inicia a proxima partida):
    def __invert(self, result):
        if result == self.names[1]:
            invertname = [self.names[1], self.names[0]]
            return invertname
        return self.names
    
    
    # Resetar o tabuleiro:
    def __reset_board(self):
        self.__tb = [['_', '_', '_'], ['_', '_', '_'], [' ', ' ', ' ']]
                
    
    # Finalizar jogo:           
    def __end_game(self, score):
        if self.score[self.names[0]] == self.score[self.names[1]]:
            print(self.__msg['no_winner'])
        else:
            print(self.__msg['winner'] % max(score, key=score.get))


    # chamar funções de jogo:
    def play(self):
        result = ''
        for i in range(0, 5):
            if result != 'exit':
                self.__reset_board()
                self.__board()
                score = self.__pscore(result)
                invertname = self.__invert(result)
                self.__board()
                result = self.__jogada(invertname)
        self.__end_game(score)



