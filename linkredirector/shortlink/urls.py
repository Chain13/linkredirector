from django.urls import path
from .views import go_redirect

urlpatterns = [
    path('<slug:slug>/', go_redirect, name='go-redirect'),
]
