from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Prewait(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.round_number == 1


class RegroupWaitPage(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number > 1

    def after_all_players_arrive(self):
        self.subsession.group_randomly(fixed_id_in_group=True)


class InstructTest2(Page):
    form_model = 'group'
    form_fields = ['test1', 'test2', 'test3', 'test4']

    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class Offer(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplier

        return dict(
            tripled_amount=tripled_amount,
            prompt='Please select an amount from 0 to {} to offer to A'.format(tripled_amount),
        )


class waitforp1(WaitPage):
    body_text = 'Waiting for player A to send an amount.'

    def is_displayed(self):
        return self.player.id_in_group == 2


class waitforp2(WaitPage):
    body_text = 'Waiting for player B to make an offer.'

    def is_displayed(self):
        return self.player.id_in_group == 1


class Accept(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 1


class ResultsWaitPage(WaitPage):
    body_text = 'Waiting to finish up the game'
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    form_model = 'player'

    def vars_for_template(self):
        return dict(tripled_amount=self.group.sent_amount * Constants.multiplier)


page_sequence = [
    Prewait,
    Intro,
    InstructTest2,
    RegroupWaitPage,
    MyPage,
    waitforp1,
    Offer,
    waitforp2,
    Accept,
    ResultsWaitPage,
    Results,
]
