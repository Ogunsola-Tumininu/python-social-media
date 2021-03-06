
from django.contrib import admin
# from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from tutorial import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect' ),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^home/', include('home.urls', namespace='home')),
    
]

#adding static file
urlpatterns += staticfiles_urlpatterns()

#adding media file
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
