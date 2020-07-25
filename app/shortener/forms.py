import logging
from django import forms


from .models import UrlMapping

logger = logging.getLogger(__name__)

class UrlMappingCreateForm(forms.Form):
    full_url = forms.URLField(required=True)
    #def __init__(self, *args, **kwargs):
    #    super(UrlMappingCreateForm, self).__init__(*args, **kwargs)
    #    self.fields['full_url'].required = True
    #
    #class Meta:
    #    model = UrlMapping
    #    fields = ['full_url',]

