from django.contrib import admin
from django.utils.safestring import mark_safe

from sporting.models import Trainer, Place, Reward, SportFederation, Section, Sport

# Register your models here.
admin.site.register(Reward)
admin.site.register(Section)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'address', 'region', 'locality', 'district', '_index', 'phone_number', 'latitude', 'longitude', 'attendance', 'capacity', 'locker_room', 'shower_room', 'jurisdiction')
    list_editable = ('director', 'address', 'region', 'locality', 'district', '_index', 'phone_number', 'latitude', 'longitude', 'attendance', 'capacity', 'locker_room', 'shower_room', 'jurisdiction')



@admin.register(SportFederation)
class FederationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'president', 'phone_number', 'email', 'latitude', 'longitude')
    list_editable = ('address', 'president', 'phone_number', 'email', 'latitude', 'longitude')


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('fio', 'trainers_photo', 'birth_date', 'is_published', 'sport')
    list_editable = ('is_published', 'sport')

    @admin.display(description='Фото')
    def trainers_photo(self, trainer: Trainer):
        if trainer.photo:
            return mark_safe(f'<img src="{trainer.photo.url}" width="50">')
        return 'Нет фото'

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_sport', 'federation', 'is_for_women', 'is_olimpic', 'sections')
    list_editable = ('type_of_sport', 'is_for_women', 'is_olimpic')

    @admin.display(description='Секции')
    def sections(self, sport: Sport):
        return ', '.join([section.name for section in sport.sections.all()])

    @admin.display(description='Секции')
    def sections(self, sport: Sport):
        return ', '.join([trainer.name() for trainer in sport.trainers.all()])
