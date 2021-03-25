from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Icecream


def icecream_list(request):
    icecreams = Icecream.objects.all()
    context = {
        'icecreams': icecreams
    }
    return render(request, 'icecream/icecream-list.html', context)

def icecream_detail(request, pk):
    icecream = get_object_or_404(Icecream, id=pk)
    rating = icecream.rating
    print(rating)
    context = {
        'icecream': icecream,
        'gold_rating': range(rating),
        'empty_rating': range(5 - rating)
    }
    return render(request, 'icecream/icecream-detail.html', context)