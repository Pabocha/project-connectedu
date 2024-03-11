from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="ça ne peut pas être modifié par l'administrateur")

    class Meta:
        model = User
        fields = ('__all__')

    def clean_password(self):
        return self.initial['password']
