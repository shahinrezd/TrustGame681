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


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125)

    gender = models.IntegerField(
        label="Please select your gender.",
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
            [4, 'I prefer not to say.'],
        ]
    )

    hin = models.IntegerField(
        label="What is your household income, including your parents",
        choices=[
            [1, 'less than 35000'],
            [2, 'Between 35,000 to including 45,000'],
            [3, 'Between 45,001 and including 65,0000'],
            [4, 'Between 65,001 up to and including 85,000'],
            [5, '85,001 and above']
        ]
    )

    fairA1 = models.IntegerField(
        choices=[
            [1, 'No'],
            [2, 'Yes'],
        ],
        label='As Player A, do you think it was fair that only Player A was endowed with 100 points, and Player B '
              'was not endowed with anything?'
    )

    fairB1 = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [2, 'No'],
        ],
        label=' In this experiment you were assigned the role of B , do you think '
              'it was fair that only Player A was endowed with 100 points, and Player B was not endowed with anything?'
    )

    fairA2 = models.IntegerField(
        label='Suppose A sent 50 points, B receives 150 After it is tripled What do you think '
        'would be a fair offer/sent amount back by B?', max=150
    )

    fairA5 = models.BooleanField(
        label='Based on the the actions of the opposite player, do you perceive their actions as fair?',
        choices=[[True, 'Yes'], [False, 'No']]
    )

    fair3 = models.IntegerField(
        label='How many other players do you believe behaved the same way as you did?',
        choices=[
            [1, 'None (<10%)'],
            [2, 'Some (10%<?>50%)'],
            [3, 'Most(50%<?>80%)'],
            [4, 'Almost All (80%<?>99%'],
            [5, 'All (>99%)']
        ]
    )
    fairA3 = models.IntegerField(
        label='What do you think is a fair amount sent by A?', max=100
    )

    fairB2 = models.IntegerField(
        label='If you were Player B and you sent/offered money back, select one of the following',
        choices=[
            [1, 'I sent back enough so that player 1 had their endowment restored'],
            [2, 'I sent back enough so that player 1 was rewarded for sending me the money'],
            [3, 'I sent back enough so that we both had the same amount at the end of the experiment'],
            [4, 'I did not send any amount back']
        ]
    )

    fairA4 = models.IntegerField(
        label='If you were  Player A and sent money, What was the MINIMUM amount sent back to you '
              'you were willing to accept? (leave 0 if you did not send any amount)', max=300
    )

    fairB3 = models.IntegerField(
        label='Since you were Player B,'
              ' what would have to be minimum amount sent to you (before being tripled) that you would be '
              'willing to send/offer the same amount back?',
        max=100
    )

    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''

    )

    crt_widget = models.IntegerField(
        label='''
        "If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?"
        '''
    )

    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
    )
