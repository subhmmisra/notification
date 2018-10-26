#forms.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from fcm_django.models import FCMDevice
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder="Username")), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder="Email")), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder="Password")), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder="Confirm Password")), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class AddUserDeviceForm(forms.ModelForm):
    model = FCMDevice
    fields = ["registration_id", "user_id", "type"]