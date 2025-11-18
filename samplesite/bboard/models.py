from django.db import models

# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(verbose_name="описание")
    price = models.FloatField(verbose_name="цена", default=0)
    published = models.DateTimeField(auto_now_add=True, 
                                     db_index=True,
                                     verbose_name="дата публикации"
                                     )
