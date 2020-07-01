from django.urls import path
from otree.urls import urlpatterns

from __CUSTOM import pages as __custom_pages

prefix = "CUSTOM"

urlpatterns.append(path(f'{prefix}/custom_view', __custom_pages.custom_view))
urlpatterns.append(path(f'{prefix}/skip_demo_setup/<session_config_name>', __custom_pages.skip_demo_setup))