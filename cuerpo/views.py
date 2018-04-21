from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
#Vistas basadas en funciones
#recibe una petición de dejame ver lo que tienes

def listadoPost(request):
    posts = Post.objects.filter(fechaPublicacion__lte = timezone.now()).order_by('fechaPublicacion')
    return render(request,'cuerpo/listadoPost.html',{'posts':posts})

