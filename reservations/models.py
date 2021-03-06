from django.db import models


class TennisCourt(models.Model):
    CITY = [
        ("Białystok", "Białystok"),
        ("Gdańsk", "Gdańsk"),
        ("Kraków", "Kraków"),
        ('Lublin', 'Lublin'),
        ("Olsztyn", "Olsztyn"),
        ("Poznań", "Poznań"),
        ("Warszawa", "Warszawa"),
        ("Wrocław", "Wrocaław"),
    ]

    name = models.CharField(max_length=64)
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    hire_price = models.IntegerField()
    city = models.CharField(choices=CITY, max_length=24)
    adress = models.CharField(max_length=128)
    equipment_rent = models.BooleanField()

    def __str__(self):
        return f'{self.city} / {self.name}'


class Reservations(models.Model):
    object = models.ForeignKey(
        TennisCourt, on_delete=models.CASCADE, related_name="reservations", blank=False, null=False
    )
    reservation_date = models.DateField()
    reservation_start = models.TimeField()
    reservation_end = models.TimeField()

    # class Meta:
    #     ordering = ['object']

    # reservation_status = models.BooleanField(default=False)
    # reservation_cost = models.IntegerField()

    def __str__(self):
        return f'{self.object}'


class AdminPanel(models.Model):
    pass


if __name__ == '__main__':
    pass
