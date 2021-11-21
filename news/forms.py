from django import forms
from django.http import request

from .models import *


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('email', 'username', 'comment')

