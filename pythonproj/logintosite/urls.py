from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^adminlogin/$',views.adminlogin),
    url(r'^authenticateadmin/$',views.authenticateadmin),
    url(r'^login/$',views.login),
    url(r'^authentication/$',views.authentication),
    url(r'^forgotpassword/$',views.forgotpassword),
    url(r'^sendmail/$',views.sendmail),
    url(r'^passwordresetform/$',views.passwordresetform),
    url(r'^resetpassword/$',views.resetpassword),
    url(r'^logout/$',views.logout),
    url(r'^logoutadmin/$',views.logoutadmin),
]