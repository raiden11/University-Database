
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Facilities import views


urlpatterns = [
    url(r'^sports$', views.sports_list),
    url(r'^library$', views.library_list),
    url(r'^sports/(?P<pk>[0-9]+)', views.sports_id),
    url(r'^library/(?P<pk>[0-9]+)', views.library_id),
]

