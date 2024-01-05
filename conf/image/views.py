from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.contrib import messages

# Create your views here.
def index(request):
    images = Image.objects.all()
    form = ImageForm()
    context = {'images': images, 'form': form}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form.save()
        messages.success(request, 'Image Uploaded successfully !')
        return redirect('/')
    return render(request, 'image/index.html', context)

def delete_image(request, pk):
    image = Image.objects.get(pk=pk)
    image.delete()
    messages.success(request, 'Image deleted!')
    return redirect('/')

def detail(request, pk):
    image = Image.objects.get(pk=pk)
    return render(request, 'image/detail.html', {'image': image})