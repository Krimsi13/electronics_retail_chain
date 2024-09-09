from django.db import models

NULLABLE = {"null": True, "blank": True}


class Manufacturer(models.Model):
    """Модель производителя."""

    MANUFACTURER_TYPE = (
        ('factory', 'Завод'),
        ('retail network', 'Розничная сеть'),
        ('sole proprietor', 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=100, verbose_name="Название производителя")

    # contacts
    email = models.EmailField(unique=True, verbose_name="Email", max_length=255)
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    supplier = models.ForeignKey("self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Поставщик")

    debt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Задолженность перед поставщиком",
                               default=0.00)

    creation_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    type = models.CharField(max_length=100, verbose_name='Тип производителя', choices=MANUFACTURER_TYPE, **NULLABLE)

    # Уровень звена от 0 до 2
    def get_level_chains(self):
        level_chains = 0
        current_manufacturer = self.supplier
        while current_manufacturer and level_chains < 2:
            level_chains += 1
            current_manufacturer = current_manufacturer.supplier
        return level_chains

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    product_model = models.CharField(max_length=100, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель",
                                     related_name="product", **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
