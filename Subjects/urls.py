
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Subjects import views


urlpatterns = [
    url(r'^$', views.subject_list),
    url(r'^(?P<pk>[0-9]+)', views.subject_id),
]








