#models.py 에 있는 객체를 활용할 것

#그래서 mainapp에 만들었다

from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']