from django.forms import (Form, CharField)


class GetCityForm(Form):
    name = CharField(max_length=64)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter city name'})
