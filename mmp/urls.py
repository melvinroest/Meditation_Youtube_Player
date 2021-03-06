"""mmp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from music_player import views as music_player_views
from pulse import views as pulse_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', music_player_views.meditation, name='meditation'),
    url(r'^meditation_settings/$', music_player_views.meditation_settings, name='meditation_settings'),

    #URLs for pulse app
    url(r'^pulse/$', pulse_views.pulse, name='pulse'),
   	url(r'^pulse/begin$', pulse_views.pulse_begin, name='pulse_begin'), 
   	url(r'^pulse/data$', pulse_views.pulse_data, name='pulse_data'),
]
