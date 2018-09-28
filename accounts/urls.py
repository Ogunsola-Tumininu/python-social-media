from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.views import password_reset, password_reset_done


urlpatterns = [
    
    url(r'^register/$', views.register, name="register"),
    url(r'^profile/$', views.view_profile, name="profile"),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name="profile_with_pk"),
    url(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
    # url(r'^change-password/$', views.change_password, name="change_password"),
    url(r'^change-password/$', auth_views.PasswordChangeView.as_view( success_url=reverse_lazy('profile'), template_name='accounts/change-password.html'), name="change_password"),
    url(r'^', include("django.contrib.auth.urls") ),
  

]