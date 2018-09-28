from django.conf.urls import url
from home.views import HomeView
from home import views 


app_name = 'home'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name="change_friend"),
]