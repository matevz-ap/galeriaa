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
    folder = forms.ChoiceField()

    class Meta:
        model = models.Gallery
        fields = ['user', 'folder']

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        folders = get_drive_folders(user_id)
        self.fields['folder'].choices = utils.folders_to_choices(folders)
        self.helper.layout = Layout(
            Hidden("user", user_id),
            Field('folder'),
            Div(
                HTML('<a href="{% url "galleries:list" %}" class="btn btn-outline-secondary flex-grow-1">Close</a>'),
                Submit('submit', 'Create', css_class='flex-grow-1'),
                css_class='d-flex justify-content-end gap-3',
            )
        )
