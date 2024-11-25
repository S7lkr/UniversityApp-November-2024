from django import forms
from django.db import models

from UniversityApp.courses.models import Course
from UniversityApp import mixins


class CourseForm(mixins.PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('slug',)

        widgets = {
            'category': forms.Select(attrs=None, choices=['Web Design']),
            # 'category': models.CharField(default='Web Design'),
        }
