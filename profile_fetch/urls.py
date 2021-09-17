from django.urls import path
from profile_fetch import views
from django.views.generic.base import TemplateView # new
  
urlpatterns = [
         path('', views.index, name='github_wala'),
]