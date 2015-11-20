from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': ''}),
        }

class PostForm2(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''}))
