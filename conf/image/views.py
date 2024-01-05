from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

# Create your views here.
def index(request):
    images = Image.objects.all()
    form = ImageForm()
    context = {'images': images, 'form': form}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form.save()
        return redirect('/')
    return render(request, 'image/index.html', context)