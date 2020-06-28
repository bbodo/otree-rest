from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from pprint import pprint


class PaymentInfo(Page):
    def vars_for_template(self):
        participant = self.participant
        return dict(redemption_code=participant.label or participant.code)
    def is_displayed(self):
        pprint(self.participant.vars)
        return True


page_sequence = [PaymentInfo]
