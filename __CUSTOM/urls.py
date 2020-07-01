from django.urls import path
from otree.urls import urlpatterns, url_patterns_from_builtin_module

from __CUSTOM import pages as __custom_pages

prefix = "CUSTOM"

urlpatterns.append(path(f'{prefix}/custom_view', __custom_pages.custom_view))
urlpatterns.append(path(f'{prefix}/skip_demo_setup/<session_config_name>', __custom_pages.skip_demo_setup))

# from django.urls import include, path
# from rest_framework import routers
# from __CUSTOM import views as __custom_views

# router = routers.DefaultRouter()
# router.register('mturk_exit_codes/subsession', __custom_views.MTurkExitCodesViewSet)
# router.register('participant', __custom_views.ParticipantViewSet)
# router.register('session', __custom_views.SessionViewSet)
# urlpatterns += [
#     path('API/', include(router.urls)),
#     #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns += url_patterns_from_builtin_module("__CUSTOM.views.rest")


