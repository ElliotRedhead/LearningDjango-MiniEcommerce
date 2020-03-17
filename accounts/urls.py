from django.conf.urls import url, include
from . import url_reset
from .views import registration, user_profile, logout, login

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="register"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]
