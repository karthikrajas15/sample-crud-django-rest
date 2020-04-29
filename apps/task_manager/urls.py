from django.urls import path
from .views import *

urlpatterns = [
    path('user-registration/', UserRegistration.as_view()),
    path('user-login/', UserLogin.as_view()),
    path('task-create/', TaskCreate.as_view()),
    path('task-update/<int:pk>/', TaskUpdate.as_view()),
    path('task-delete/<int:pk>/', TaskDelete.as_view()),
]