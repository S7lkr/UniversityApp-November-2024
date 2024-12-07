from django import forms
from UniversityApp.lessons.models import Lesson


class LessonBaseForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ("course",)


class LessonAddForm(LessonBaseForm):
    pass


class LessonDeleteForm(LessonBaseForm):
    class Meta(LessonBaseForm.Meta):
        model = Lesson
        exclude = ('title', 'description', 'readme', 'course')
