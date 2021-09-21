from django.urls import path
from App1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as v
from django.conf.urls import url
from django.views.static import serve
  

urlpatterns=[
    path('',views.home,name="home"),
    #path('questions',views.questions,name="questions"),
    path('addQuestions',views.addQuestions,name='addQuestions'),
    path('exam',views.exam,name="exam"),
    path('userreg',views.userRegistration,name="userrreg"),
    path('rg/',views.usrreg,name="reg"),
    path('login/',v.LoginView.as_view(template_name="ht1/login.html"),name="login"),
    path('logout/',v.LogoutView.as_view(template_name="ht1/logout.html"),name="lgo"),
    path('pfle/',views.pfle,name="pf"),
    #path('pfupd/',views.pfleupd,name="pfup"),
    #path('profileupdate/<int:id>/',views.profileUpdate,name="profileupdate"),
    path('chge/',views.changepwd,name="chpd"),

    path('roltype/',views.rolereq,name="rlrq"),
    path('gvper/',views.gveperm,name='gvpm'),
    path('gvup/<int:t>/',views.gvupdate,name="gvup"),
    path('fdb/',views.feedback,name="fd"),
    path('deleteuser/<int:id>/',views.deleteuser,name="deleteuser"),

]