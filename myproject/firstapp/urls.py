from django.urls import path
from firstapp import views

urlpatterns = [
    path('',views.indexfunction,name="index"),
    #path('user',views.userfunction,name="user"),
    path('user1',views.user1function,name="user1"),
    path('user/<int:id>',views.userfunction1,name="user_1"),
    path('user/<int:a>/<int:b>',views.addfunction,name="add"),
    #path('userpage/',views.userpage,name="userpage"),
    #path('index/',views.indexpage,name="index"),
    path('app/',views.apppage,name="app"),
    path('adminpage/',views.adminpage,name="admin"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('viewusers/',views.viewusers,name="viewusers"),
    path('deleteuser/<int:id>',views.deleteuser,name="deleteuser"),
    path('alogout/',views.alogout,name="alogout"),
    path('contact/',views.contactuspage,name="contact"),
    path('userreg/',views.userreg,name="userreg"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('birthday/',views.birthday,name="birthday"),
    path('contactme/',views.contactme,name="contactme"),
    path('regsuccess/',views.regsuccess,name="regsuccess"),
    path('payment/',views.payment,name="payment"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('questions/',views.questions,name="questions"),
    path('wedding/',views.wedding,name="wedding"),
    path('farewell/',views.farewell,name="farewell"),
    path('fests/',views.fests,name="fests"),
    path('final/',views.final,name="final"),
    path('checkuser/',views.checkuser,name="checkuser"),
    path('checkadmin/',views.checkadmin,name="checkadmin")


]