from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('test/', views.test, name='all')
]