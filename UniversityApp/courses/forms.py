from django import forms
from django.db import models

from UniversityApp.courses.models import Course
from UniversityApp import mixins


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('slug',)

        widgets = {
            'category': forms.Select(attrs=None, choices=['Web Design']),
            # 'category': models.CharField(default='Web Design'),
        }


class CourseCreateForm(mixins.PlaceholderMixin, mixins.DisabledFieldsMixin,  CourseForm):
    # disabled_fields_set = ('category',)
    pass


class CourseEditForm(CourseForm):
    pass


class CourseDeleteForm(mixins.DisabledFieldsMixin, CourseForm):
    # disabled_fields_set = ('name', 'category',)

    class Meta:
        model = Course
        fields = ('name', 'category',)
