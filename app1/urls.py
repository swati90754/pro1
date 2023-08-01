from django.urls import path
from .views import student_view, display_view, update_view, home_view, delete_view
urlpatterns = [
    path('sv/',student_view, name='student_url'),
    path('dv/',display_view, name='display_url'),
    path('dev/<int:pk>/',delete_view, name='delete_url'),
    path('hv/',home_view, name='home_url'),
    path('uv/<int:pk>/', update_view, name='update_url'),
  
 ]