from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from django_resized import ResizedImageField

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Trainer(models.Model):
    fio = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    experience = models.DateField(null=True, blank=True)
    attendance = models.PositiveIntegerField(null=True, blank=True)
    photo = ResizedImageField(size=[110, 110], upload_to=f'trainers/{slugify(fio)}', null=True, blank=True,
                              force_format='PNG', keep_meta=False, quality=100)
    rewards = models.ManyToManyField('Reward',
                                     verbose_name='Награды',
                                     related_name='awarded', null=True, blank=True)  # many-to-many relation with Reward
    place = models.ManyToManyField('Place',
                                   verbose_name='Место преподавания',
                                   related_name='trainers', null=True, blank=True)  # many-to-many relation with Place
    is_published = models.BooleanField(default=True)
    sport = models.ForeignKey('Sport', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Спорт', related_name='trainers')

    def name(self):
        first_name, last_name, fathers_name = self.fio.split()
        return f'{first_name} {last_name[0]}.{fathers_name[0]}.'

    def __str__(self):
        return self.fio


class Reward(models.Model):
    name = models.CharField(max_length=100)
    reward_date = models.DateField()

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = PhoneNumberField(max_length=20, region='RU', null=True, blank=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)], default=None, null=True, blank=True)
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null=True, blank=True)
    attendance = models.PositiveIntegerField(null=True, blank=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    locker_room = models.BooleanField(default=False, null=True, blank=True)
    shower_room = models.BooleanField(default=False, null=True, blank=True)
    jurisdiction = models.CharField(max_length=300, null=True, blank=True, verbose_name='Учредитель')

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название секции')
    trainers = models.ManyToManyField('Trainer', verbose_name='Тренеры', related_name='sections')
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True, blank=True, related_name='sections')
    federation = models.ForeignKey('SportFederation', on_delete=models.SET_NULL, null=True, blank=True, related_name='sections')
    sport = models.ForeignKey('Sport', on_delete=models.SET_NULL, null=True, blank=True, related_name='sections')

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Вид спорта')
    type_of_sport = models.CharField(max_length=100, null=True, blank=True, verbose_name='Тип спорта')
    federation = models.OneToOneField('SportFederation', on_delete=models.SET_NULL, null=True, blank=True, related_name='sport')
    is_olimpic = models.BooleanField(default=False, null=True, blank=True, verbose_name='Олимпиада')
    is_for_women = models.BooleanField(default=False, null=True, blank=True, verbose_name='Для женщин')

    def __str__(self):
        return self.name

class SportFederation(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название федерации')
    address = models.CharField(max_length=100, verbose_name='Адрес федерации')
    president = models.CharField(max_length=100, verbose_name='Президент федерации')
    phone_number = PhoneNumberField(max_length=20, region='RU', null=True, blank=True, verbose_name='Телефон федерации')
    phone_number2 = PhoneNumberField(max_length=20, region='RU', null=True, blank=True, verbose_name='Телефон федерации 2')
    email = models.EmailField(max_length=100, verbose_name='Email федерации', null=True, blank=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)], default=None, null=True,
                                 blank=True)
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null=True,
                                  blank=True)


    def __str__(self):
        return self.name