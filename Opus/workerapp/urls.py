from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.loginpage,name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('loginview/', views.login_view, name="loginview"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signupview/', views.signupview, name="signupview"),
    path('signup/', views.signup, name="signup"),
    path('userloginview/', views.userloginview, name="userloginview"),
    path('userdashboard/', views.userdashboard, name="userdashboard"),
    path('usersignupview/', views.usersignupview, name="usersignupview"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('userlogin/', views.userlogin,name="userlogin"),
    path('requestwork/', views.requestwork, name="requestwork"),
    path('user_logout_view/', views.user_logout_view, name="user_logout_view"),
    path('acceptbooking/', views.acceptbooking, name="acceptbooking"),
    path('dashboard1/', views.dashboard1, name="dashboard1"),
    path('usersignupview/', views.usersignupview, name="usersignupview"),

]