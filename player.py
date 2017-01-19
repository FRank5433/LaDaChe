# -*- coding: utf-8 -*-


class AiPlayer:
    def __init__(self):
        self.my_cards = []

    def get_a_card(self, card):
        self.my_cards.append(card)

    def play_a_card(self):
        card = self.my_cards[0]
        self.my_cards.pop(0)
        return card
