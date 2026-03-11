from django.urls import path
from home import views
from home.views import cgpa_calculator, delete_subject, edit_subject, result, login_page, custom_logout, register_page

urlpatterns = [
    path('', cgpa_calculator, name='cgpa_calculator'),
    path('edit/<int:subject_id>/', edit_subject, name='edit_subject'),
    path('delete/<int:subject_id>/', delete_subject, name='delete_subject'),
    path('result/', result, name='result'),
    
    path('login/' , login_page, name='login'),
    path('logout/', custom_logout, name="logout"),
    path('register/', register_page, name='register'),
 
     
]