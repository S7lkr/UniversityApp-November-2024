from django import forms
from UniversityApp.common.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Add comment...'})
        }
        labels = {
            'content': '',
        }
