from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register,profile, TenantSignUpView, AgentSignUpView


urlpatterns = [

    path('login_form/', views.login_form, name='login_form'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),

    # path('signup/',register, name='register'),
    # path('profile/',profile, name='profile'),
    # path('signup/tenant/', TenantSignUpView.as_view(), name='tenant_signup'),
    # path('signup/agent/', AgentSignUpView.as_view(), name='agent_signup'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

]
