from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)


class CustomAllAuthSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomAllAuthSignUpForm, self).__init__(*args, **kwargs)
        self.fields['photo'] = forms.ImageField()
        
    
    def save(self, request,*args, **kwargs):
        
        user = super(CustomAllAuthSignUpForm, self).save(request)
        user.photo = self.cleaned_data['photo']
        user.save()
        return user