from django.db.models import Model, ImageField
from django.db.models import CharField, DecimalField, TextField, ForeignKey, CASCADE, TextChoices

# Create your models here.

class Job(Model):
    class Type(TextChoices):
        FULL = 'fulltime', 'Fulltime'
        REMOTE = 'remote', 'Remote'
        CONTRACT = 'contract', 'Contract'
        WFH = 'wfh', 'WFH'

    title = CharField(max_length=100)
    type = CharField(max_length=10, choices=Type.choices, default=Type.FULL)
    address = CharField(max_length=100)
    country = CharField(max_length=100)

    def __str__(self):
        return self.title



class Category(Model):
    title = CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(Model):
    class Type(TextChoices):
        HOT = "hot", "Hot"
        NEW = "new", "New"
        SOLD = "sold", "Sold"

    title = CharField(max_length=100)
    price = DecimalField(decimal_places=2, max_digits=10)
    category = ForeignKey(Category, on_delete=CASCADE, related_name="products")
    description = TextField()
    tag = CharField(choices=Type.choices, max_length=10)
    image_url = CharField(max_length=255, default="")
    rating = DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.title



class Plan(Model):
    title = CharField(max_length=100)
    price = DecimalField(decimal_places=2, max_digits=10)
    text_1 = TextField()
    text_2 = TextField()
    text_3 = TextField()


class OnlyProduct(Model):
    class Size(TextChoices):
        XS = "xs", "XS"
        S = "s", "S"
        M = "m", "M"
        L = "l", "L"
        XL = "xl", "XL"
        XXL = "xxxl", "XXL"

    main_image = ImageField(upload_to="images/")
    title = CharField(max_length=100)
    price = DecimalField(decimal_places=2, max_digits=10)
    available = DecimalField(decimal_places=2, max_digits=10)
    description = TextField()
    size = CharField(choices=Size.choices, max_length=10)

    def __str__(self):
        return self.title

class Images(Model):
    image = ImageField(upload_to="images/")
    product = ForeignKey(OnlyProduct, on_delete=CASCADE, related_name="images")


from django.db.models import Model, CharField, DecimalField, PositiveBigIntegerField


class Car(Model):
    name = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    speed = DecimalField(max_digits=6, decimal_places=2)
    km = PositiveBigIntegerField()

    def __str__(self):
        return self.name


