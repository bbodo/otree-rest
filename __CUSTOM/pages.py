# In my_app.pages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from otree import session as otree_session
from pprint import pprint

def custom_view(request):
    return HttpResponse('hi bro')

def skip_demo_setup(request, session_config_name):
    # borrowing code from otree.session
    session = otree_session.create_session(session_config_name, num_participants = None, is_demo=True)
    # borrowing code from otree.views.admin.
    anonymous_url = request.build_absolute_uri(reverse('JoinSessionAnonymously', args=[session._anonymous_code]))
    pprint(anonymous_url)
    print(F"You are skipping the setup page of {session_config_name}.")
    return HttpResponseRedirect(anonymous_url)