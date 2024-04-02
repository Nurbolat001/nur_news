from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# forms.py

from django import forms
from .models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['photo', 'title', 'publication_date', 'description']


from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['photo', 'title', 'publication_date', 'description']

from django import forms
from .models import News

class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['photo', 'title', 'publication_date', 'description']
