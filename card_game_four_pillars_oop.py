# Author: Aman Kharwal
from abc import ABC, abstractmethod
from random import shuffle

class BasePlayer(ABC): 
    @abstractmethod
    def __init__(self, player_name):
        self.player_name = player_name
        self.wins = 0

class BaseGame(ABC): 
    @abstractmethod
    def play_game(self):
        pass

    @abstractmethod
    def winner(self, player1, player2):
        pass

class GameCard:
    card_suits = ["spades", "hearts", "diamonds", "clubs"]
    card_values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "Jack", "Queen", "King", "Ace"]

    def __init__(self, card_value, card_suit):
        self.card_value = card_value
        self.card_suit = card_suit
        

    def __lt__(self, c2):
        if self.card_value < c2.card_value:
            return True
        if self.card_value == c2.card_value:
            return self.card_suit < c2.card_suit
        return False

    def __gt__(self, c2):
        if self.card_value > c2.card_value:
            return True
        if self.card_value == c2.card_value:
            return self.card_suit > c2.card_suit
        return False

    def __repr__(self):
        return f"{self.card_values[self.card_value]} of {self.card_suits[self.card_suit]}"

class CardDeck:
    def __init__(self):
        self.cards = [GameCard(v, s) for v in range(2, 15) for s in range(4)]
        shuffle(self.cards) 

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class Player(BasePlayer):  
    def __init__(self, player_name):
        super().__init__(player_name)
        self.card = None 

class CardGame(BaseGame): 
    def __init__(self):
        name1 = input("Player1 name: ")
        name2 = input("Player2 name: ")
        self.game_deck = CardDeck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def round_winner(self, winner_name):
        print(f"{winner_name} wins this round")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f"{p1n} drew {p1c}, {p2n} drew {p2c}")

    def play_game(self): 
        print("Card War Begins!")
        while len(self.game_deck.cards) >= 2:
            response = input("Type q to quit or any key to continue: ")
            if response == 'q':
                break

            p1c = self.game_deck.draw_card()
            p2c = self.game_deck.draw_card()
            self.player1.card = p1c
            self.player2.card = p2c

            self.draw(self.player1.player_name, p1c, self.player2.player_name, p2c)

            if p1c > p2c:
                self.player1.wins += 1
                self.round_winner(self.player1.player_name)
            else:
                self.player2.wins += 1
                self.round_winner(self.player2.player_name)

        final_winner = self.winner(self.player1, self.player2)
        print(f"War is over. {final_winner} wins")

    def winner(self, player1, player2): 
        if player1.wins > player2.wins:
            return player1.player_name
        elif player2.wins > player1.wins:
            return player2.player_name
        else:
            return "It was a tie!"

if __name__ == "__main__":
    game = CardGame()
    game.play_game()
