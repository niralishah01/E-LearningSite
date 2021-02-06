from django.conf.urls import url
from . import views 

urlpatterns=[
    url(r'^getregsdetails/$',views.getregsdetails),
    url(r'^addregsdetails/$',views.addregsdetails),
    url(r'^delete/$',views.delete),
]