from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Icecream
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def icecream_list(request):
    icecreams = Icecream.objects.all()
    paginator = Paginator(icecreams, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page':page,
        'paginator':paginator,
    }
    return render(request, 'icecream/icecream-list.html', context)

@login_required
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