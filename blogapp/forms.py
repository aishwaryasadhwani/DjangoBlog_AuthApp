from django import forms
from django.contrib.auth.models import User
from blogapp.models import PostBlog

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')
        widgets = {'password':forms.PasswordInput()}

class PostBlogForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ('title','description','file')
        widgets = {'description':forms.Textarea(attrs={'rows':5,'cols':5})}
