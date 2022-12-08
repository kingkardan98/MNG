from django import forms
from .models import User

class UserForm(forms.ModelForm):
    availability = forms.FloatField(required=True, 
                                    label='', 
                                    widget=forms.NumberInput(
        attrs={
            'label': 'availability',
            'placeholder': 'Availability'
            }
        )
    )

    spendable = forms.FloatField(required=True, 
                                 label='', 
                                 widget=forms.NumberInput(
        attrs={
            'label': 'spendable',
            'placeholder': 'Spending limit'
            }
        )
    )

    username = forms.CharField(required=True, 
                               label='', 
                               widget=forms.TextInput(
        attrs={
            'label': 'username',
            'placeholder': 'Username'
            }
        )
    )

    email = forms.CharField(required=True, 
                            label='',
                            widget=forms.EmailInput(
        attrs={
            'label': 'email',
            'placeholder': 'Email'
            }
        )
    )

    password = forms.CharField(required=True, 
                               label='', 
                               widget=forms.PasswordInput(
        attrs={
            'label': 'password',
            'placeholder': 'Password'
            }
        )
    )

    confirm_password = forms.CharField(required=True, 
                                       label='', 
                                       widget=forms.PasswordInput(
        attrs={
            'label': 'confirm_password',
            'placeholder': 'Confirm password'
            }
        )
    )

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