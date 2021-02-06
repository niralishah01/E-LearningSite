from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^gotohome/$',views.gotohome),
    url(r'^adminhome/$',views.adminhome),
    url(r'^getcoursedetails/$',views.getcoursedetails),
    url(r'^addcoursedetails/$',views.addcoursedetails),
    url(r'^deletecourse/$',views.deletecourse),
    url(r'^delete/$',views.delete),
    url(r'^deletecoursecontent/$',views.deletecoursecontent),
    url(r'^getcoursecontent/$',views.getcoursecontent),
    url(r'^addcoursecontent/$',views.addcoursecontent),
    # url(r'^viewcourses/$',views.viewcourses),
    url(r'^searchcourses/$',views.searchcourses),
    url(r'^showcourses/$',views.showcourses),
    url(r'^getvideocoursecontent/$',views.getvideocoursecontent),
    url(r'^addvideocoursecontent/$',views.addvideocoursecontent),
    
]