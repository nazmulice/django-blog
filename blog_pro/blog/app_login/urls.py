from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('user_change/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('add-picture/', views.add_pro_pic, name='add_pro_pic'),
    path('change-picture/', views.change_pro_pic, name='change_pro_pic'),
]