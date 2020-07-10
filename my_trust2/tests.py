from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield (pages.Intro)

        if self.subsession.round_number == 1:

            yield (pages.InstructTest2, {'test1': False, 'test2': False, 'test3': False, 'test4': True})

        if self.player.id_in_group == 1:
            yield (pages.MyPage, {"sent_amount": 40})
            yield (pages.Accept, {'offer_accepted': False})

        if self.player.id_in_group == 2:
            yield (pages.Offer, {'sent_back_amount': 80})

        yield pages.Results
