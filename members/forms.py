from django import forms
from .models import Member

from .member_create_data_check import checkSuite

class MemberForm(forms.ModelForm):
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
            'label': 'Confirm password',
            'placeholder': 'Confirm password'
            }
        )
    )

    class Meta:
        model = Member
        fields = [
            'availability',
            'spendable',
            'username',
            'email',
            'password'
        ]

    def clean(self):
        cleaned_data = super(MemberForm, self).clean()

        data_dict = {
            'password': cleaned_data.get("password"),
            'confirm_password': cleaned_data.get("confirm_password"),
            'spendable': cleaned_data.get("spendable"),
            'availability': cleaned_data.get("availability")
        }

        errorList, relations, error_messages = checkSuite(data_dict)
        for error in errorList:
            self.add_error(relations[error], error_messages[error])
        
        return cleaned_data