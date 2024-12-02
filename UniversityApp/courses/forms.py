from django import forms
from UniversityApp.courses.models import Course
from UniversityApp import mixins


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('slug', 'lector',)
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': '',
            'category': '',
            'description': '',
            'start_date': '',
            'credits': '',
            'duration': '',
            'photo': '',
        }


class CourseCreateForm(mixins.PlaceholderMixin, CourseBaseForm):
    # disabled_fields_set = ('category',)
    pass


class CourseEditForm(CourseBaseForm):
    pass


class CourseDeleteForm(mixins.DisabledFieldsMixin, forms.ModelForm):
    disabled_fields_set = ('name', 'category',)

    class Meta:
        model = Course
        fields = ('name', 'category',)
