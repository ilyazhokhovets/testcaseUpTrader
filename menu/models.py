from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class Field(models.Model):
    name = models.CharField('name', max_length=127)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=127, editable=False, )
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE )
    level = models.SmallIntegerField('Level',editable=False,)

    def __str__(self):
        return f'{self.level}: {self.name}'

    def save(self, *args, **kwargs):
        if self.parent:
            self.url = f'{self.parent.url}{self.name}/'
            self.menu = self.parent.menu
            self.level = self.parent.level+1
        else:
            self.url = f'{self.menu.name}/{self.name}/'
            self.level = 0
        super(Field, self).save(*args, **kwargs)

    # def clean(self):
    #     if self.parent:
    #         if self.parent.menu != self.menu:
    #             raise ValidationError(f'Родитель находится в меню {self.parent.menu.name}')
    #     super(Field, self).clean()


class Menu(models.Model):
    name = models.CharField('name', max_length=127)

    def __str__(self):
        return self.name