from .views import HomeTemplateView
from django.urls import path

urlpatterns = [
    path('', HomeTemplateView.as_view()),
]