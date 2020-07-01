### FROM otree.views.rest - FOR POST REQUESTS
import json

import vanilla
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers

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

### my own
from __CUSTOM.urls import prefix

class Session(BaseRESTView):

    url_pattern = f'{prefix}/api/sessions/'

    def inner_post(self, **kwargs):
        session = create_session(**kwargs)
        room_name = kwargs.get('room_name')
        if room_name:
            channel_utils.sync_group_send_wrapper(
                type='room_session_ready',
                group=channel_utils.room_participants_group_name(room_name),
                event={},
            )
        return HttpResponse(session.code)
    
    def get(self, request):
        return JsonResponse(data=list(otree.models.session.Session.objects.values()), safe=False)

