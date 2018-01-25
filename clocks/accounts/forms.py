from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols':80, 'rows': 20}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio')
