# -*- coding: utf-8 -*-

import dealer
import player


class Table:
    def __init__(self):
        self.discard_pile = []
        self.dealer = dealer.Dealer()
        self.player_in_table = [player.AiPlayer(), player.AiPlayer(), player.AiPlayer(), player.AiPlayer(),
                                player.AiPlayer(), player.AiPlayer(), player.AiPlayer(), player.AiPlayer()]

    def have_fun(self):
        # 创建牌组并洗牌、发牌
        self.dealer.create_cards()
        self.dealer.get_cards()
        self.dealer.shuffle_card_pile()
        self.dealer.deal_cards(self.player_in_table)

        # 开始打牌
        round_number = 0
        while True:
            # 轮流出牌
            round_number += 1
            print("----第%s局----" % round_number)
            for player_ix in self.player_in_table:
                if len(player_ix.my_cards) == 0:
                    continue
                card = player_ix.play_a_card()
                print("玩家打出了" + card)
                self.discard_pile.append(card)
                print("场上牌局面: " + str(self.discard_pile))
                for i, temp_player_ix in enumerate(self.player_in_table):
                    print("玩家%s有牌%s张;" % (i + 1, len(temp_player_ix.my_cards)), end="")
                print("")
                self.dealer.check_player_state(self.player_in_table)
                self.dealer.check_discard_pile(player=player_ix, discard_pile=self.discard_pile)
