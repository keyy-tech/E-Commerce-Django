from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, UsersProfile


class CustomUserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
        ]

        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control p-2",
                    "placeholder": "Email",
                    "aria-describedby": "emailHelp",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control p-2",
                    "placeholder": "Password",
                    "aria-describedby": "passwordHelp",
                }
            ),
            "confirm_password": forms.PasswordInput(
                attrs={"class": "form-control p-2", "placeholder": "Confirm Password"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control p-2", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control p-2", "placeholder": "Last Name"}
            ),
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        try:
            validate_password(password)
        except ValidationError as e:
            self.add_error("password", e)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")

        return cleaned_data


class UsersProfileForm(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = ["profile_picture", "address", "phone_number", "date_of_birth"]

        widgets = {
            "profile_picture": forms.FileInput(
                attrs={"class": "form-control p-2", "placeholder": "Profile Picture"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control p-2", "placeholder": "Address"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control p-2", "placeholder": "Phone Number"}
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-control p-2",
                    "placeholder": "Date of Birth(mmmm dd, yyyy)",
                }
            ),
        }
