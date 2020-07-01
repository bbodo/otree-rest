from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range, safe_json
)
from .exit_codes import hash_and_save_csv, hash_and_save_json


author = 'Bodo Brägger'

doc = """
An example app for MTurk exit code generation.
After the creating a session in the app using either the sessions tab or the demo tab
a new file named as 'YEAR-MONTH-DAY_Hour_Minute_Second_SessionCode.csv' will appear
in the project directory
"""
# json_data = ""

class Constants(BaseConstants):
	name_in_url = 'mturk_exit_codes'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	def creating_session(self):
		# You can change the URL or leave it blank for a simple AccessCode, ExitCode file.
		hash_and_save_csv(self.session.participant_set.all(), self.session.code, "")
		# global json_data
		self.session.vars['codes'] = hash_and_save_json(self.session.participant_set.all(), self.session.code, "")

	def vars_for_admin_report(self):
		if('codes' not in self.session.vars):
			self.session.vars['codes'] = hash_and_save_json(self.session.participant_set.all(), self.session.code, "")
		return {'AccessExit': safe_json(self.session.vars['codes'])}

class Group(BaseGroup):
	pass

class Player(BasePlayer):
	pass
