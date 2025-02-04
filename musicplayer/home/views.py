from django.shortcuts import render
from .models import Song 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def paginate_queryset(queryset, request, per_page=1):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page", 1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj

def index(request):
    
    songs = Song.objects.all()

    page_obj = paginate_queryset(songs, request, per_page=1)

    return render(request, "index.html", {"page_obj":page_obj})   
   