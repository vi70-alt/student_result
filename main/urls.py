from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_redirect, name='welcome'),
    path('home/', views.home, name='home'),  
    path('after_login/', views.after_login, name='after_login'),
    path('add_student/', views.add_student, name='add_student'),
    path('enter_result/', views.enter_result, name='enter_result'),
    path('my_results/', views.student_results, name='my_results'),
    path('logout/', views.logout_view, name='logout'),
]
