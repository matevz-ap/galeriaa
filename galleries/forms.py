from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML
from crispy_forms.layout import Div
from crispy_forms.layout import Field
from crispy_forms.layout import Hidden
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django import forms

from . import models


class GalleryForm(forms.ModelForm):
    folder = forms.CharField(
        widget=forms.Select(attrs={"id": "folder-autocomplete", "autocomplete": "off"}),
        help_text="Select a folder from your Google Drive",
    )

    class Meta:
        model = models.Gallery
        fields = ["user", "folder", "name"]

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop("user_id")
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Hidden("user", self.user_id),
            Field("name", placeholder="Name your gallery"),
            Field("folder", placeholder="Select a folder", style="max-width: 450px"),
            Div(
                HTML(
                    '<a href="{% url "galleries:list" %}" class="btn btn-light shadow-sm bg-white flex-grow-1">Close</a>'
                ),
                Submit("submit", "Create", css_class="flex-grow-1 shadow-sm"),
                css_class="d-flex justify-content-end gap-3",
            ),
        )

    def is_valid(self) -> bool:
        if models.Gallery.objects.filter(user_id=self.user_id).count() > 20:
            self.add_error(None, "You have reached the maximum number of galleries")
            return False
        return super().is_valid()


class GalleryChangeForm(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Name your gallery", "class": "form-control"}
            )
        }
