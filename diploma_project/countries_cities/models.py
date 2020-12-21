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
    capital = models.CharField(null=True, max_length=50, verbose_name='Столица Страны')
    population = models.IntegerField(null=True, verbose_name='Население')
    foundation_date = models.IntegerField(null=True, verbose_name='Год основания')
    official_languages = models.CharField(null=True, max_length=150, verbose_name='Языки Страны')
    qoute = models.TextField(null=True)
    qoute_by = models.CharField(null=True, max_length=150, verbose_name='Автор цитаты')
    background_image = models.ImageField(null=True, upload_to=load_photo, verbose_name="Бекграунд фото")
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
    foundation_date = models.IntegerField(null=True, verbose_name='Год основания')
    population = models.IntegerField(null=True, verbose_name='Население')
    description = models.TextField(null=True, verbose_name='Описание Города')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='country', verbose_name='Название страны')
    image = models.ImageField(null=True, upload_to=load_photo, verbose_name="Фото Города")    
    slug = models.SlugField(null=True, max_length=150, verbose_name='Ссылка')


    def __str__(self):
        return self.name


    def image_tag(self):
        if self.image:
            city_photo = self.image.url
            return mark_safe(f'<img src={city_photo} width="200" height="150"')
        else:
            'Photo not found'
    image_tag.allow_tags = True
    

    class Meta:
        db_table = "city"
        verbose_name = "Город"
        verbose_name_plural = "Города"





class ArticlePreview(models.Model):


    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}", file_type])
        return file_name.format(
            self.name,
            self.image
        )


    name = models.CharField(max_length=250, verbose_name='Название статьи')
    image = models.ImageField(upload_to=load_photo, max_length=250, verbose_name="Фото статьи")


    class Meta:
        db_table = "article_preview"
        verbose_name = "article"
        verbose_name_plural = "articles"


class ArticleText(models.Model):


    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}", file_type])
        return file_name.format(
            self.article,
            self.photo
        )


    text = models.TextField(verbose_name='Текст статьи', null=True)
    photo = models.ImageField(max_length=250, upload_to=load_photo, verbose_name="Фото статьи", null=True)
    article = models.ForeignKey(ArticlePreview, on_delete=models.CASCADE, related_name='article', verbose_name='Текст статьи', null=True)


    class Meta:
        db_table = "article_text"
        verbose_name = "text"
        verbose_name_plural = "text"


    




