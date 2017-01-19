# -*- coding: utf-8 -*-

import copy
import random

CARD_LIST = []


class Dealer:
    def __init__(self):
        self.card_pile = []

    @staticmethod
    def create_cards():
        global CARD_LIST
        color_of_card = ['Spade', 'Heart', 'Diamond', 'Club']
        number_of_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for color_ix in color_of_card:
            for number_ix in number_of_card:
                CARD_LIST.append(color_ix + " " + number_ix)

    def get_cards(self):
        self.card_pile = copy.deepcopy(CARD_LIST * 100)

    def shuffle_card_pile(self):
        random.shuffle(self.card_pile)

    def deal_cards(self, player_list):
        card_pile_ix = 0
        while True:
            for player_ix in player_list:
                player_ix.get_a_card(self.card_pile[card_pile_ix])
                card_pile_ix += 1
            if card_pile_ix == len(self.card_pile):
                break

    @staticmethod
    def check_player_state(player_list):
        winner_number = 0
        winner_it = 0
        for i, player_ix in enumerate(player_list):
            if len(player_ix.my_cards) != 0:
                winner_number += 1
                if winner_number == 1:
                    winner_it = i + 1
            if winner_number >= 2:
                break
        if winner_number == 1:
            print("胜者是玩家%s" % winner_it)
            exit()

    @staticmethod
    def check_discard_pile(player, discard_pile):
        last_card = discard_pile[-1]
        same_card_it = 0
        for card_it in range(-2, -len(discard_pile) - 1, -1):
            if discard_pile[card_it][-1] == last_card[-1]:
                same_card_it = card_it
            else:
                pass

        if same_card_it == 0:
            return 0
        else:
            for it in range(same_card_it, 0):
                player.get_a_card(discard_pile[it])
            for ix in range(abs(same_card_it)):
                discard_pile.pop()
