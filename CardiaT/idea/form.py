from django import forms
from .models import Idea
from .models import Comments

class Blog_creation(forms.ModelForm):
    class Meta:
        model=Idea
        fields=['title','content','date_posted']



class Comment(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['description']