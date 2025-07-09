from django.shortcuts import get_object_or_404, redirect
from .models import ShortLink

# Create your views here.

def go_redirect(request, slug):
    link = get_object_or_404(ShortLink, slug=slug)
    return redirect(link.target_url)
