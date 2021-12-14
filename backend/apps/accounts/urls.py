from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register,profile,loginView, TenantSignUpView, AgentSignUpView


urlpatterns = [

    path('login_form/', views.login_form, name='login_form'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('tenant_signup/', views.TenantSignUpView.as_view(), name='tenant-signup'),
    path('agent_signup/', views.AgentSignUpView.as_view(), name='agent-signup'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
