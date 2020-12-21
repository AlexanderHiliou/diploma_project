
from django.db import models
from countries_cities.models import Country, City


class Gallary(models.Model):


    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}_{}", file_type])
        return file_name.format(
            self.country,
            self.city,
            self.name,
        )


    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_2 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_3 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_4 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_5 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_6 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_7 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_8 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_9 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    photo_10 = models.ImageField(upload_to=load_photo, null=True, verbose_name='Фотография')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'gallary'
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
