from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.http import JsonResponse
# Import this function to get the exit code for a single player
from .exit_codes import sha_hash #, aes_encrypt,
#from .models import json_file

class Checkout(Page):
    def vars_for_template(self):
        return {'exit_code' : sha_hash(self.participant.code)[0:8]}

# class AccessExit():
#     test = JsonResponse({'AccessExit': json_file}, safe=False)

page_sequence = [
    Checkout
]
