from django.http import HttpResponse

from rest_framework import viewsets, permissions

from .serializers import *
from mturk_exit_codes import models as mturk_exit_codes_models
import otree
#from otree import models as otree_models

from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator

@login_required
def custom_view(request, *args, **kwargs):
    return HttpResponse('hi bro')

# THE DECORATORS ARE TO USE OTREES BUILTIN LOGIN SCREEN
# @method_decorator(login_required, name='dispatch')
class ParticipantViewSet(viewsets.ModelViewSet):
    # THIS WOULD BE A BASIC HTML LOGIN REQUEST, not sure how to get this to work
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = otree.models.Participant.objects.all().order_by('id_in_session')
    serializer_class = ParticipantSerializer
    

# @method_decorator(login_required, name='dispatch')
class SessionViewSet(viewsets.ModelViewSet):
    queryset = otree.models.Session.objects.all()
    serializer_class = SessionSerializer

# class PlayerViewSet(viewsets.ModelViewSet):
#     queryset = otree.models.BasePlayer.objects.all()
    # serializer_class = SessionSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = otree.models.BaseGroup.objects.all()