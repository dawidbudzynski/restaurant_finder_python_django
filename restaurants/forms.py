from django.forms import (Form, CharField)


class GetCityForm(Form):
    name = CharField(max_length=64)
