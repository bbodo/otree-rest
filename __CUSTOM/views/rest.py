import json

import vanilla
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

import otree
from otree.channels import utils as channel_utils
import otree.bots.browser
from otree.models_concrete import (
    ParticipantVarsFromREST,
    BrowserBotsLauncherSessionCode,
)
from otree.room import ROOM_DICT
from otree.session import create_session
from otree.views.abstract import BaseRESTView

class RESTCreateSession(BaseRESTView):

    url_pattern = r'^api/cool/sessions/$'

    def inner_post(self, **kwargs):
        '''
        Notes:
        - This allows you to pass parameters that did not exist in the original config,
        as well as params that are blocked from editing in the UI,
        either because of datatype.
        I can't see any specific problem with this.
        '''
        session = create_session(**kwargs)
        room_name = kwargs.get('room_name')
        if room_name:
            channel_utils.sync_group_send_wrapper(
                type='room_session_ready',
                group=channel_utils.room_participants_group_name(room_name),
                event={},
            )
        return HttpResponse(session.code)
