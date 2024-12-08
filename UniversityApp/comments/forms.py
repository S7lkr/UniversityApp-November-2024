from django import forms
from UniversityApp.comments.models import Comment
from UniversityApp.mixins import DisabledFieldsMixin


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


class CommentDeleteForm(DisabledFieldsMixin, forms.ModelForm):
    disabled_fields_set = ('content',)

    class Meta:
        model = Comment
        fields = ('content',)
