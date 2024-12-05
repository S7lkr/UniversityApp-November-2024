from django import forms
from UniversityApp.lessons.models import Lesson


class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ("course",)
