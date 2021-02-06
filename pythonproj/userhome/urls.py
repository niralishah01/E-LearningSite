from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^gotouserhome/$',views.gotouserhome),
    url(r'^categorizedcourses/$',views.categorizedcourses),
    url(r'^enroll/$',views.enroll),
    url(r'^viewprofile/$',views.viewprofile),
    url(r'^showtext/$',views.showtext),
    url(r'^showvideo/$',views.showvideo),
    url(r'^viewcourse/$',views.viewcourse),
    url(r'^mycourses/$',views.mycourses),
    url(r'^updatestatus/$',views.updatestatus),
    url(r'^viewstatus/$',views.viewstatus),
    url(r'^searchcourses/$',views.searchcourses),
]