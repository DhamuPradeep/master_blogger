from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.forms import TextInput,ModelForm,Textarea,FileInput,ImageField

class WritingForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title','body','user','image']

        widgets = {
            'title':TextInput(attrs={
                'class':"form-control",
                'style': 'font-size:30px; width:51%',
                'placeholder':'Title of the Post...',
            }),
            'body': Textarea(attrs={
                'class':"form-control",
                'style':'font-size:18px; padding: 12px 20px;width:50%; height:280px',
                'placeholder':'Write a Post...'
            }),
            'user': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size:30px; width:51%',
                'placeholder': 'Your name...',
            }),
        }

class UpdateUserForm(forms.ModelForm):

    first_name = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    username = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

