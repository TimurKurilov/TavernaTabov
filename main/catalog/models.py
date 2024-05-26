from django.db import models

# Create your models here.
class ElectroGuitar(models.Model):
    
    COLOR_CHOICES = [
        ('Зеленый', 'Зеленый'),
        ('Красный', 'Красный'),
        ('Синий', 'Синий'),
        ('Черный', 'Черный'),
        ('Белый', 'Белый'),
        ('Серый', 'Серый'),
    ]
    
    FORM_CHOICES = [
        ('Телекастер', 'Телекастер'),
        ('Леспол', 'Леспол'),
        ('Суперстрат', ' Суперстрат'),
        ('СГ', 'СГ'),
        ('Эксплорер', 'Эксплорер'),
        ('Стратокастер', 'Стратокастер'),
    ]
    BRAND_CHOICES = [
        ('Yamaha', 'Yamaha'),
        ('Ibanez', 'Ibanez'),
        ('Fender', 'Fender'),
        ('Gibson', 'Gibson'),
    ]
    
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, blank=True, null=False)
    form = models.CharField(max_length=20, choices=FORM_CHOICES, blank=True, null=False)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, blank=True, null=False)