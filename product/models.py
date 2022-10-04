from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):

    def validate_amount(value):
        if value % 5 != 0:
            raise ValidationError(
                _('%(value)s is not multiple of 5'),
                params={'value': value},
            )

    amountAvailable = models.IntegerField()
    cost = models.IntegerField(validators=[validate_amount])
    productName = models.CharField(max_length=256)
    sellerId = models.IntegerField()
