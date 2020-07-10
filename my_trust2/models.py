from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from otree.models import player

author = 'shahin'

doc = """
positive & negative reciprocity
"""


class Constants(BaseConstants):
    name_in_url = "Reciprocity"
    players_per_group = 2
    num_rounds = 5
    endowment = c(100)
    multiplier = 3
    offer_increment = c(0.5)
    offered_choices = currency_range(c(0), endowment * multiplier, c(0.5))
    offer_choice_count = len(offered_choices)
    p1_payoff_rejected = c(5)
    p2_payoff_rejected = c(0)
    instructions_template = 'my_trust2/instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=c(0), max=Constants.endowment, label="how much did you want to send group B"
    )

    sent_back_amount = models.CurrencyField(
        min=c(0), label="Please select an amount to offer to Player A"
    )

    def sent_back_amount_max(self):
        return self.sent_amount * Constants.multiplier

    offer_accepted = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']], label='Do you accept this offer?'
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
            p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount
            print('p1.payoff', p1.payoff)
            print('p2.payoff', p2.payoff)
        else:
            p1.payoff = (Constants.endowment - self.sent_amount)
            p2.payoff = Constants.p2_payoff_rejected
            print('p1.payoff', Constants.p1_payoff_rejected)
            print('p2.payoff', Constants.p2_payoff_rejected)

    test1 = models.BooleanField(
        choices=[[True, 'Player A'], [False, 'Player B']], label='Who makes the first move?'
    )

    test2 = models.BooleanField(
        choices=[[True, '0'], [False, 'Any amount left over']], label='What is Player Bs'
                                                                      ' payoff if A rejects their final '
                                                                      'offer? '
    )

    test3 = models.BooleanField(
        choices=[[True, 'The remainder of my endowment'],
                 [False, 'Nothing']],
        label='What is player As payoff if A reject Bs offer?'

    )

    test4 = models.BooleanField(
        choices=[[True, 'Yes'], [False, 'No']], label='Do you HAVE to send/offer any amount to the other player?'
    )


class Player(BasePlayer):

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
