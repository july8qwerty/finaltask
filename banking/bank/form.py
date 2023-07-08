from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import register


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = register
		fields = ("name", "psw", "cpsw")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user