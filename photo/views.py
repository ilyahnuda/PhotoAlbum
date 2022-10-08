from django.shortcuts import render, redirect
from .models import *


# Create your views here.


def gallery(requests):
    category = requests.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(requests, 'photos/gallery.html', context=context)


def view_photo(requests, pk):
    photo = Photo.objects.get(pk=pk)
    context = {'photo': photo}
    return render(requests, 'photos/photo.html', context)


def add_photo(requests):
    categories = Category.objects.all()

    if requests.method == 'POST':
        data = requests.POST
        image = requests.FILES.get('image')
        print(data)
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(category=category, description=data['description'], image=image)
        return redirect('gallery')
    context = {'categories': categories}
    return render(requests, 'photos/add.html', context=context)
