from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'hin']


class Fair(Page):
    form_model = 'player'
    form_fields = ['fairA1', 'fairA2', 'fairA3', 'fairA4', 'fairA5', 'fair3', ]

    def is_displayed(self):
        return self.player.id_in_group == 1


class Fair2(Page):
    form_model = 'player'
    form_fields = ['fairB1', 'fairB2', 'fairB3', 'fairA3', 'fairA2', 'fairA5', 'fair3']

    def is_displayed(self):
        return self.player.id_in_group == 2


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


class Thank(Page):
    pass


page_sequence = [Demographics, Fair, Fair2, CognitiveReflectionTest, Thank]
