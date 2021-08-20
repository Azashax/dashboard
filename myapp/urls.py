from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('students/', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
    path('mentors/', views.mentors, name='mentors'),
    path('lessons/', views.lessons, name='lessons'),

    path('action_order/<str:pk>/', views.action_page, name='action_page'),
    path('delete_order/<str:pk>/', views.delete_page, name='delete_page'),
]