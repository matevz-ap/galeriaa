from galleries.services import get_drive_folders
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Field
from crispy_forms.layout import Hidden
from crispy_forms.layout import Layout
from crispy_forms.layout import Div
from crispy_forms.layout import HTML
from . import models
from . import utils


class GalleryForm(forms.ModelForm):
    folder = forms.CharField(widget=forms.Select(attrs={'id': 'folder-autocomplete', "autocomplete": 'off'}))

    class Meta:
        model = models.Gallery
        fields = ['user', 'folder', 'name']

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Hidden("user", user_id),
            Field('name', placeholder="Name your gallery"),
            Field('folder', placeholder="Select a folder"),
            Div(
                HTML('<a href="{% url "galleries:list" %}" class="btn btn-light shadow-sm bg-white flex-grow-1">Close</a>'),
                Submit('submit', 'Create', css_class='flex-grow-1 shadow-sm'),
                css_class='d-flex justify-content-end gap-3',
            )
        )
