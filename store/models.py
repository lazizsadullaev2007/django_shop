from django.db import models
from django.urls import reverse
from users.models import CustomUser
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# категория
# kategoriya


class Subcategory(models.Model):
    name = models.CharField(verbose_name="Название подкатегории", max_length=150, unique=True)
    slug = models.SlugField(verbose_name='Ссылка подкатегории')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_total(self):
        return self.products.all().count()

    def get_absolute_url(self):
        return reverse('store:subcategory_products', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


# models for product

class Product(models.Model):
    def make_preview_path(self, filename):
        """Создаем папку с фотками для заставок по названию продукта."""
        return f'products/preview/{filename}'

    class ProductOptionChoices(models.TextChoices):
        NEW = ('new', 'new')
        SALE = ('sale', 'sale')
        SOLD = ('sold', 'sold')

        __empty__ = ''

    name = models.CharField(max_length=150, unique=True, verbose_name='Название продукта')
    short_description = models.TextField(max_length=200, verbose_name='Краткое описание продукта')
    full_description = models.TextField(verbose_name='Полное описание продукта')
    quantity = models.PositiveSmallIntegerField(default=10, verbose_name='Кол-во')
    price = models.IntegerField(verbose_name='Стоимость')
    sku = models.CharField(max_length=50, verbose_name='Артикул')
    preview = models.ImageField(verbose_name="Заставка", upload_to=make_preview_path)
    condition = models.CharField(max_length=10, choices=ProductOptionChoices.choices,
                                 verbose_name='Состояние', blank=True)
    slug = models.SlugField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория',
                                    related_name='products')

    def __str__(self):
        return self.name

    def get_preview(self):
        if self.preview:
            return self.preview.url

    def get_absolute_url(self):
        return reverse('store:detail', kwargs={'slug': self.slug})

    def add_to_cart(self):
        return reverse('cart:to_cart', kwargs={'product_id': self.pk, 'action': 'add'})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    def make_image_path(self, filename):
        return f'products/images/{filename}'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт',
                                related_name='images')
    image = models.ImageField(verbose_name='Фото', upload_to=make_image_path)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Продукт')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews',
                               verbose_name='Автор')
    content = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
