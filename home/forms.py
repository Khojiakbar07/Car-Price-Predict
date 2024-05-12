from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['CarCompanyName', 'fueltype', 'highwaympg', 'citympg', 'horsepower', 'curbweight']
