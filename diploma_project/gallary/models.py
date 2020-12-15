from django.db import models
from countries_cities.models import Country, City


class Gallary(models.Model):


    def load_photo(self):
        pass


    photo = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'gallary'
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'