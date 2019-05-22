from django.forms import CharField, Form


class GetCityForm(Form):
    city = CharField(max_length=64, required=True)
    street = CharField(max_length=64, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].label = ''
        self.fields['city'].widget.attrs.update({'placeholder': 'City', 'class': "form-control"})
        self.fields['street'].label = ''
        self.fields['street'].widget.attrs.update({'placeholder': 'Street', 'class': "form-control"})
