from django.forms import Form, CharField, DecimalField, IntegerField
from apps.models import Car


class CarForm(Form):
    name = CharField(max_length=100, min_length=1,
                     error_messages={"min_length": "Name must have at least 1 character!"})
    price = DecimalField(max_digits=10, decimal_places=2, min_value=0,
                         error_messages={"min_value": "Price cannot be negative!"})
    speed = DecimalField(max_digits=6, decimal_places=2, min_value=0, error_messages={"min_value": "Do not enter negative numbers!"})
    km = IntegerField(min_value=0, error_messages={"min_value": "Do not enter negative numbers!"})

    def save(self):
        if self.is_valid():
            return Car.objects.create(**self.cleaned_data)
        return None


