from django.urls import path
from otree.urls import urlpatterns, url_patterns_from_builtin_module

from __CUSTOM import pages as __custom_pages

prefix = "CUSTOM"

urlpatterns.append(path(f'{prefix}/custom_view', __custom_pages.custom_view))
urlpatterns.append(path(f'{prefix}/skip_demo_setup/<session_config_name>', __custom_pages.skip_demo_setup))

urlpatterns += url_patterns_from_builtin_module("__CUSTOM.views.rest")


router = routers.DefaultRouter()
# router.register('players', __custom_views.PlayerViewSet)
router.register('participants', __custom_views.ParticipantViewSet)
router.register('sessions', __custom_views.SessionViewSet)
urlpatterns += [
    path('API/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
