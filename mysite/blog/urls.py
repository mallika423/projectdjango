from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    #url('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]