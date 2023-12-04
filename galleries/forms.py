from galleries.services import get_drive_folders
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
        self.helper.add_input(Submit('submit', 'Submit'))
