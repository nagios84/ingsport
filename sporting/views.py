from django.shortcuts import render
from django.views.generic import ListView

from .models import Trainer, Place, Reward, SportFederation, Section, Sport


# Create your views here.
def main(request):
        context = {'slogan': 'Найди свой вид спорта!', 'weprovide': 'В справочнике секций и залов найдутся занятия по вкусу'}
        trainers = Trainer.objects.all()
        sports = Sport.objects.all().order_by('sections')[:8]
        context.update({'trainers': trainers, 'sports': sports})
        return render(request, 'sporting/index.html', context=context)


class Trainers(ListView):
    model = Trainer
    template_name = 'sporting/trainers.html'
    paginate_by = 12
