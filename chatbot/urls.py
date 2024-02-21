from django.urls import path
from . import views

# url for chatbot view
urlpatterns = [
    path('', views.chatbot, name='chatbot')
]