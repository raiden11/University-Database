
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Students import views


urlpatterns = [
    url(r'^$', views.student_list),
    url(r'^(?P<pk>[0-9]+)', views.student_id),
]














