from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "due_date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full border rounded px-3 py-2"}),
            "description": forms.Textarea(attrs={"class": "w-full border rounded px-3 py-2"}),
            "status": forms.Select(attrs={"class": "w-full border rounded px-3 py-2"}),
            "due_date": forms.DateInput(attrs={"class": "w-full border rounded px-3 py-2", "type": "date"}),
        }
