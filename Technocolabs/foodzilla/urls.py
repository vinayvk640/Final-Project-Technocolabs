from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomeViwe.as_view()), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),    
    path('accounts/login/', views.AccountsView.as_view(), name='accounts'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('update_item/', views.UpdateItemView.as_view(), name="update_item"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
          name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
          name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),
          name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
          name='reset_password_complete'),


]

