from django.urls import path
from .views import Login, SingUp

urlpatterns = [
    path('login/', Login.as_view()),
    path('singup/', SingUp.as_view()),
]