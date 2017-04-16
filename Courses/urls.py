
from django.conf.urls import url
from Courses import views


urlpatterns = [
    url(r'^$', views.course_list),
    url(r'^(?P<pk>[0-9]+)', views.course_id),
]









