from rest_framework import serializers

import otree
#from otree.api import models as otree_models

from pprint import pprint
pprint(vars(otree.models.Session).keys())

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = otree.models.Participant
        # fields = '__all__'
        exclude = []
        """
            fields = [
            'code',
            'id_in_session',
            'is_browser_bot',
            'is_on_wait_page',
            'label',
            'mturk_assignment_id',
            'mturk_worker_id',
            'payoff',
            'session',
            'time_started',
            'url',
            'vars',
            'visited',
            '_browser_bot_finished',
            '_current_app_name',
            # '_current_form_page_url',
            '_current_page_name',
            '_index_in_pages',
            '_index_in_subsessions',
            '_is_bot',
            '_last_page_timestamp',
            '_last_request_timestamp',
            '_max_page_index',
            '_round_number',
            '_waiting_for_ids',
        ]"""

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = otree.models.Session
        exclude = []
        """ fields = [
            'participation_fee',
            'real_world_currency_per_point',
            'use_browser_bots',
            'is_mturk',
            'get_subsessions',
            'get_participants',
            'config',
            'label',
            'experimenter_name',
            'code',
            'mturk_expiration',
            'archived',
            'comment',
            '_anonymous_code',
            'num_participants',
            'participant_set',
            'mturk_exit_codes_subsession',
            'mturk_exit_codes_group',
            'mturk_exit_codes_player',
            'payment_info_subsession',
            'payment_info_group',
            'payment_info_player',
        ] """

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = otree.models.BasePlayer