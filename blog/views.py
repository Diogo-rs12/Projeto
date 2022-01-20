from django.shortcuts import render
from django.utils import timezone
from .models import Post, Fatos, Aleatorio
from django.shortcuts import render, get_object_or_404



def home(request):
    return render(request, 'blog/home.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def fatos_list(request):
    fatos = Fatos.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/fatos_list.html', {'fatos': fatos})

def fatos_detail(request, pk):
    fato = get_object_or_404(Fatos, pk=pk)
    return render(request, 'blog/fatos_detail.html', {'fato': fato})

def aleatorio_list(request):
    aleatorios = Aleatorio.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/aleatorio_list.html', {'aleatorios': aleatorios})

def aleatorio_detail(request, pk):
    aleatorio = get_object_or_404(Aleatorio, pk=pk)
    return render(request, 'blog/aleatorio_detail.html', {'aleatorio': aleatorio})