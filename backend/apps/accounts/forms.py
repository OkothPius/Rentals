# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User
#
# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget= forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#
#
# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#     email = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control"
#             }
#         )
#     )
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'is_agent', 'is_user')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Tenant, Agent

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class TenantSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_tenant = True
        user.save()
        tenant = Tenant.objects.create(user=user)
        return user

class AgentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=200)
    designation = forms.CharField(max_length=200)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_agent = True
        user.save()
        agent = Agent.objects.create(user=user)
        agent.phone = self.cleaned_data.get('phone')
        agent.designation = self.cleaned_data.get('designation')


        agent.save()

        return agent
