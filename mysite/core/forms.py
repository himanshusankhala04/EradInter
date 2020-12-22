from django import forms
from django.utils.safestring import mark_safe

class SignupForm(forms.Form):
    name = forms.CharField(label=mark_safe('Name'), max_length=40)
    ph_no= forms.CharField(label=mark_safe('<br /><br />Phone no '))
    add = forms.CharField(label=mark_safe('<br /><br />Address '), max_length=100)
    u_id = forms.CharField(label=mark_safe('<br /><br />User Id '), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    widgets = {
            'password': forms.PasswordInput(),
        }