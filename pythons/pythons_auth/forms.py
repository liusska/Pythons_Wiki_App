from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)


class SignInForm(forms.Form):
    user = None

    username = forms.CharField(
        max_length=15,
    )
    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(),
    )

    def clean(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('Username and/or password incorrect')

    def save(self):
        return self.user
