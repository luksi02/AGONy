from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from AGONy.models import Event, Origin
from rpg.models import Monster, Hero


class HeroCreateForm(forms.ModelForm):

    class Meta:
        model = Hero
        fields = ['name']


class MonsterCreateForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = '__all__'


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class OriginCreateForm(forms.ModelForm):
    class Meta:
        model = Origin
        fields = '__all__'


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Password is too short')


def check_if_has_number(value):
    if not any(x for x in value if x.isdigit()):
        raise ValidationError('Password need to include a digit')


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                validators=[validate_password, check_if_has_number],
                                help_text='Hasło ma być dłuższe niż 8')
    password2 = forms.CharField(label='re-Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        data = super().clean()
        pass1 = data.get('password1')
        if pass1 is not None and pass1 != data.get('password2'):
            raise ValidationError('Passwords are not the same!')
        return data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'}),
                               required=False)

