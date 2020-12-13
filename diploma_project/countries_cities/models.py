from django.db import models
from django.utils.safestring import mark_safe


class Country(models.Model):


    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["Flags/{}_flag", file_type])
        return file_name.format(
            self.name,
        )


    name = models.CharField(max_length=150, verbose_name='Название Страны')
    description = models.TextField(verbose_name='Описание Страны')
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')
    icon = models.ImageField(upload_to=load_photo, verbose_name="Флаг Страны")


    def __str__(self):
        return self.name


    def image_tag(self):
        if self.icon:
            country_photo = self.icon.url
            return mark_safe(f'<img src={country_photo} width="200" height="150"')
        else:
            'Photo not found'
    image_tag.allow_tags = True


    class Meta:
        db_table = "country"
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

class City(models.Model):
    
    
    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}", file_type])
        return file_name.format(
            self.country,
            self.name,
        )



    name = models.CharField(max_length=150, verbose_name='Название Города')
    foundation_date = models.IntegerField(verbose_name='Год основания')
    population = models.IntegerField(verbose_name='Население')
    description = models.TextField(verbose_name='Описание Города')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='country', verbose_name='Название страны')
    image = models.ImageField(upload_to=load_photo, verbose_name="Фото Города")    
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')


    def __str__(self):
        return self.name


    def image_tag(self):
        if self.image:
            city_photo = self.image.url
            return mark_safe(f'<img src={city_photo} width="200" height="150"')
        else:
            'Photo not found'
    image_tag.allow_tags = True


    def show_image(self):
        pass


    def get_links(self):
        pass


    def get_location(self):
        pass
    

    class Meta:
        db_table = "city"
        verbose_name = "Город"
        verbose_name_plural = "Города"

# Create your models here.
