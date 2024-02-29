from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('change_data/',views.change_user_data,name='change_data'),
    # path('pass change/',views.pass_change,name='pass_change'),
    # path('pass change2/',views.pass_change2,name='pass_change2'),
    # path('change data/',views.change_user_data,name='change_data'),
]