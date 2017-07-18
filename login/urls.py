from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[0-9]+)/submit/$',views.authenticate('kgs\dcorrea','KGS-305-dc#'), name='submit'),
]
