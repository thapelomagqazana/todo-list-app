from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

    
    # def clean_title(self):
    #     title = self.cleaned_data.get("title")
    #     # Add custom validation logic for the title field
    #     if len(title) < 5:
    #         raise forms.ValidationError("Title must be at least 5 characters long.")
    #     return title