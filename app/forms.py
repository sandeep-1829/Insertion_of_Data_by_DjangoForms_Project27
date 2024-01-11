from django import forms
from django.core import validators


def validate_for_s(value):
    if value.lower().startswith('s'):
        raise forms.ValidationError('Value startswith s...')

def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('Data is < 5..')


class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_s,validators.MaxLengthValidator(7)])
    Sprincipal=forms.CharField(validators=[validate_for_s,validators.MinLengthValidator(4)])
    Slocation=forms.CharField()
    Email=forms.EmailField()
    ReenterEmail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        e=self.cleaned_data['Email']
        re=self.cleaned_data['ReenterEmail']
        if e!=re:
            raise forms.ValidationError('Emails are not matched...')

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('botcatcher..')

    




