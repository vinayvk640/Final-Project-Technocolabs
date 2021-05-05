from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeViwe.as_view(), name='home'),
    #path('contact/', views.contact, name='contact'),
    path('login/', views.LoginView.as_view(), name='login'),
    #path('accounts/', views.accounts, name='accounts'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    

]

