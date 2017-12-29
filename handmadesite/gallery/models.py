from django.db import models

# Create your models here.
class ProductModel(models.Model):
    BROOCH = 'B'
    KEYKEEER = 'K'
    PRODUCT_TYPE_CHOICE = (
        ('B', 'Брошки'),
        ('K', 'Ключницы')
    )
    product_name = models.CharField(max_length=128)
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE_CHOICE, default=BROOCH)
    description  = models.TextField()
    price        = models.DecimalField(max_digits=7, decimal_places=2)
    created  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductPictureModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return '{}-{}'.format(self.product.product_name, self.id)