from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Company(models.Model):
    class CompanyType(models.TextChoices):
        DISTRIBUTOR = "DISTRIBUTOR"
        PRODUCTION = "PRODUCTION"
        STORE = "STORE"

    class Category(models.TextChoices):
        GROCERIES = "GROCERIES"
        ELECTRONICS = "ELECTRONICS"
        STATIONERY = "STATIONERY"
        FURNITURE = "FURNITURE"
        CONSTRUCTION = "CONSTRUCTION"

    name = models.CharField(max_length=100)
    mobile_num = models.IntegerField(
        validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)]
    )
    company_name = models.CharField(max_length=100, unique=True)
    company_type = models.CharField(
        choices=CompanyType.choices, default=CompanyType.DISTRIBUTOR, max_length=15
    )
    category = models.CharField(
        choices=Category.choices, default=Category.GROCERIES, max_length=15
    )
    budget = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(2000)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
