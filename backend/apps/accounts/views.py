from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

from .models import User, Tenant, Agent, Profile
from .forms import TenantSignUpForm, AgentSignUpForm, UserUpdateForm

def register(request):
    return render(request, 'accounts/register.html')

def login_form(request):
	return render(request, 'accounts/login.html')

def logoutView(request):
	logout(request)
	return redirect('home')


def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if user.is_admin or user.is_superuser:
				return redirect('dashboard')
			elif user.is_agent:
			    return redirect('agent_dashboard')
			elif user.is_tenant:
			    return redirect('tenant_dashboard')
			else:
			    return redirect('login_form')
		else:
		    messages.info(request, "Invalid Username or Password")
		    return redirect('login_form')

class TenantSignUpView(CreateView):
    model = User
    form_class = TenantSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tenant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tenant_dashboard')

class AgentSignUpView(CreateView):
    model = User
    form_class = AgentSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('agent_dashboard')
        

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        # p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            # p_form.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        # p_form = ProfileUpdateForm(instance = request.user.profile)


    context = {
        'u_form': u_form,
        # 'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)

def index(request):
    return render(request, 'accounts/index.html')
