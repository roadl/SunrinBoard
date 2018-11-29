from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment

class Postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text', 'category')

        labels = {
            'title': '제목',
            'text': '내용',
            'category':'카테고리'
        }

class Commentform(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        
        labels = {
            'text':'내용'
        }
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',  'password']

        labels = {
            'username':'사용자명',
            
            'password':'비밀번호'
        }
