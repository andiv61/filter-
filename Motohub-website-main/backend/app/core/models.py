from django.db import models

class Motorcycle(models.Model):
    SPORT = 'SP'
    CRUISER = 'CR'
    ENDURO = 'EN'
    TYPE_CHOICES = [
        (SPORT, 'Спортивный'),
        (CRUISER, 'Круизер'),
        (ENDURO, 'Эндуро'),
    ]
    
    model = models.CharField("Модель", max_length=100)
    type = models.CharField("Тип", max_length=2, choices=TYPE_CHOICES, default=CRUISER)
    year = models.IntegerField("Год выпуска")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)
    
    def __str__(self):
        return f"{self.model} ({self.year})"
