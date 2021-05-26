import random

# from cardgame.models import Player, Statistic, GameData

COLORS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'





class CurrentPlayer:
    def __init__(self, player_id, name):
        self.id = player_id
        self.name = name
        self.position = 0
        self.winner = False

    def __str__(self):
        return f'{self.name}:{self.position}'


class NewGame:
    def __init__(self, players_num: int, deck_len: int, board_len: int):
        self.game_temp_data = {}
        self.deck = deck_len
        self.board = board_len
        self.card = ''
        self.game_participants = players_num
        self.who_turn = 0
        self.game_status = False
        self.is_draw = False
        self.turn_count = 0

    @property
    def game_participants(self):
        return self._game_participants

    @game_participants.setter
    def game_participants(self, players_num):
        players_list = []
        self._game_participants = []
        for i in players_list:
            new_player = CurrentPlayer(i.id, i.name)
            self._game_participants.append(new_player)

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, deck_len):
        self._deck = []
        for i in range(deck_len):
            color = random.choice(COLORS)
            self._deck.append(color)

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board_len):
        self._board = []
        for i in range(board_len):
            color = random.choice(COLORS)
            self._board.append(color)

    def save_game_stance(self):
        self.game_temp_data.deck = self.deck
        self.game_temp_data.board = self.board
        self.game_temp_data.card = self.card
        self.game_temp_data.game_participants = self.game_participants
        self.game_temp_data.who_turn = self.who_turn
        self.game_temp_data.game_status = self.game_status
        self.game_temp_data.is_draw = self.is_draw
        self.game_temp_data.turn_count = self.turn_count

        return True

    def next_card(self):
        check_double = random.randint(0, 1)
        self.card = self.deck.pop()
        if check_double == 1:
            self.card = self.card * 2

    def next_position(self, position):
        for i, j in enumerate(self.board[position + 1:]):
            if self.card[0] == j:
                position = i + position
                if len(self.card) > 1:
                    for n, m in enumerate(self.board[i + 1:]):
                        if self.card[0] == m:
                            position = n + position
                            return position
                    position = len(self.board)
                    return position
                return position
        position = len(self.board)
        return position

    def check_winner(self):
        if len(self.deck) > 0:
            if self.game_participants[self.who_turn].position >= (len(self.board) - 1):
                self.game_participants[self.who_turn].winner = True

                self.game_status = False
                self.save_game_stance()
                return False
            self.save_game_stance()
            return True

        self.is_draw = True
        self.game_status = False
        self.save_game_stance()
        return False

    def next_turn(self):
        self.turn_count += 1
        self.next_card()
        current_user = self.game_participants[self.who_turn]
        current_user.position = self.next_position(current_user.position)
        if self.check_winner():
            if self.who_turn < (len(self.game_participants) - 1):
                self.who_turn += 1
                self.save_game_stance()
                return self.who_turn
            self.who_turn = 0
            self.save_game_stance()
            return self.who_turn
        return False

def new_cardgame():
    gamestance = NewGame(4, 10, 50)
    print(gamestance.game_status)

new_cardgame()