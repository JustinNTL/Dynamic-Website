from django.shortcuts import render

from blog.models import posts

# Create your views here.

def home(request):
   entries = posts.objects.all()[:10]
   return render(request, 'index.html', {'posts' : entries})
