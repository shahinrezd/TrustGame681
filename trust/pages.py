from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


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

class Introduction(Page):
    pass


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplier

        return dict(
            tripled_amount=tripled_amount,
            prompt='Please an select amount from 0 to {} to send back to A'.format(tripled_amount),
        )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return dict(tripled_amount=self.group.sent_amount * Constants.multiplier)


page_sequence = [
    Prewait,
    Introduction,
    RegroupWaitPage,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
