from django import forms
from .models import Idea
from .models import Comments

class Blog_creation(forms.ModelForm):
    class Meta:
        model=Idea
        fields=['title','content','date_posted','tag_name']



class Comment(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['description']

# class Tag(forms.ModelForm):
#     class Meta:
#         model=Tags
#         fields=['tag_name']
