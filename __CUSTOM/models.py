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

from rest_framework import serializers
from ...trust.models import models

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.group
        fields = ('sent_amount', 'sent_back_amount')