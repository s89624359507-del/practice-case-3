from django.db import models


class UserName(models.Model):
    """Модель для хранения имён пользователей. Одно поле — name."""
    name = models.CharField(max_length=50, verbose_name='Имя')

    def __str__(self):
        return self.name
