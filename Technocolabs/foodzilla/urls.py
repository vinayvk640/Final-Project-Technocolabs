from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomeViwe.as_view()), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),    
    path('accounts/login/', views.AccountsView.as_view(), name='accounts'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    

]

