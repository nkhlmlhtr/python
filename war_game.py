'''This Module is a popular card game called War !!'''
import random
suits = ('Hearts','Spades','Diamonds','Clubs')
ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,
          'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':11,'Queen':12,'King':13}

class Card:
    '''This is Card class which represents a single card in a deck.'''
    def __init__(self,suit,rank):
        self.suit = suit #Heart/Spade/Diamond/Club
        self.rank = rank #Ace/Jack/Queen/King/Any Number
        self.value = values[rank]

    def __str__(self):
        return self.rank+' of '+self.suit

    def __len__(self):
        return self.value


class Deck:
    '''This is a deck class which represents a deck of cards.'''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def __str__(self):
        return '\n'.join([str(card) for card in self.all_cards])

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        '''Method to shuffle the deck of cards'''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''Deal cards to both players one by one'''
        return self.all_cards.pop()



class Player():
    '''This is a player class which represents
    each player who is playing the game'''
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        '''Remove a card from the list of cards'''
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        '''Add cards to the list of cards'''
        if isinstance(new_cards,list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


if __name__ == '__main__':
    player_one = Player('One')
    player_two = Player('Two')

    new_deck = Deck()
    new_deck.shuffle()

    ##Distributing shuffled cards between 2 players
    for i in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    print(f'Player {player_one.name} has {len(player_one.all_cards)} cards.')
    print(f'Player {player_two.name} has {len(player_two.all_cards)} cards.')

    GAME_ON = True
    ROUND_NUMBER = 0

    while GAME_ON:
        ROUND_NUMBER+=1
        print(f'Round {ROUND_NUMBER}:\n')
        if len(player_one.all_cards) <= 0:
            print(f'Player {player_one.name} out of cards. {player_two.name} wins !!')
            GAME_ON = False
            break
        if len(player_two.all_cards) <= 0:
            print(f'Player {player_two.name} out of cards. {player_one.name} wins !!')
            GAME_ON = False
            break

        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
        else:
            AT_WAR = True
            while AT_WAR:
                for i in range(5):
                    try:
                        player_one_cards.append(player_one.remove_one())
                    except IndexError:
                        print(f'Player {player_one.name} is out of cards. '
                              f'{player_two.name} wins !!')
                        AT_WAR = False
                        GAME_ON = False
                        break
                    try:
                        player_two_cards.append(player_two.remove_one())
                    except IndexError:
                        print(f'Player {player_two.name} is out of cards. '
                              f'{player_one.name} wins !!')
                        AT_WAR = False
                        GAME_ON = False
                        break
                if player_one_cards[-1].value > player_two_cards[-1].value:
                    player_one.add_cards(player_one_cards)
                    player_one.add_cards(player_two_cards)
                    AT_WAR = False
                    break
                if player_two_cards[-1].value > player_one_cards[-1].value:
                    player_two.add_cards(player_one_cards)
                    player_two.add_cards(player_two_cards)
                    AT_WAR = False
                    break
