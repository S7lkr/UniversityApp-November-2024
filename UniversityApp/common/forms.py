from django import forms
from UniversityApp.common.models import Comment


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Add comment...'})
        }
        labels = {
            'content': '',
        }


class CommentAddForm(CommentBaseForm):
    pass


class CommentEditForm(CommentBaseForm):
    pass


class CommentDeleteForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ()
