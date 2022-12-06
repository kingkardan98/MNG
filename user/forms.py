from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    availability = forms.FloatField()
    spendable = forms.FloatField()

    class Meta:
        model = User
        fields = [
            'availability',
            'spendable',
            'username',
            'email',
            'password'
        ]

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        spendable = cleaned_data.get("spendable")
        availability = cleaned_data.get("availability")

        if password != confirm_password:
            self.add_error('confirm_password',
                "Passwords don't match."
            )

        if spendable > availability:
            self.add_error('spendable',
                "Spending limit can't be higher than availability."
            )

        return cleaned_data