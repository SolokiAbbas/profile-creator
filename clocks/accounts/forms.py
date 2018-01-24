from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = user
        fields = ('username', 'email', 'password', 'bio')
        widgets = { 'bio': Textarea(attrs={'cols':80, 'rows': 20})}
