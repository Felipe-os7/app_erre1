from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Collection, Painting
from .forms import SubmissionForm


def gallery_list(request):
    collections = Collection.objects.all()
    qs = Painting.objects.all().order_by('-created_at')

    # filters
    collection_id = request.GET.get('collection')
    if collection_id:
        qs = qs.filter(collection_id=collection_id)
    for_sale = request.GET.get('for_sale')
    if for_sale == '1':
        qs = qs.filter(is_for_sale=True)
    elif for_sale == '0':
        qs = qs.filter(is_for_sale=False)
    category = request.GET.get('category')
    if category:
        qs = qs.filter(category=category)

    paginator = Paginator(qs, 9)
    page = request.GET.get('page')
    paintings = paginator.get_page(page)

    return render(request, 'galeria/gallery_list.html', {
        'collections': collections,
        'paintings': paintings,
    })


def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    paintings = collection.paintings.order_by('-created_at')
    paginator = Paginator(paintings, 9)
    page = request.GET.get('page')
    paintings_page = paginator.get_page(page)
    return render(request, 'galeria/collection_detail.html', {
        'collection': collection,
        'paintings': paintings_page,
    })


@login_required
def submit_art(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'galeria/submit_success.html')
    else:
        form = SubmissionForm()
    return render(request, 'galeria/submit.html', {'form': form})


@login_required
def delete_painting(request, pk):
    """Elimina una pintura"""
    painting = get_object_or_404(Painting, pk=pk)
    if request.method == 'POST':
        painting_title = painting.title
        painting.delete()
        messages.success(request, f'Pintura "{painting_title}" eliminada exitosamente.')
        return redirect('galeria:gallery_list')
    return render(request, 'galeria/delete_confirm.html', {
        'item': painting,
        'item_type': 'pintura',
        'cancel_url': 'galeria:gallery_list'
    })
