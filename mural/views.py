from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Mural
from .forms import MuralSubmissionForm, MuralQuoteForm
from contacto.models import ContactMessage


def mural_list(request):
    murals = Mural.objects.order_by('-created_at')
    return render(request, 'mural/mural_list.html', {'murals': murals})


@login_required
def submit_mural(request):
    if request.method == 'POST':
        form = MuralSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mural ha sido publicado.')
            return redirect('mural:submit_mural_success')
    else:
        form = MuralSubmissionForm()
    return render(request, 'mural/submit.html', {'form': form})


def submit_mural_success(request):
    return render(request, 'mural/submit_success.html')


def send_standard_mural_quote(request):
    """Redirige al formulario de cotización de mural"""
    return redirect('mural:mural_quote')


def mural_quote(request):
    """Vista para el formulario de cotización de mural"""
    if request.method == 'POST':
        form = MuralQuoteForm(request.POST)
        if form.is_valid():
            # Si el usuario está autenticado, asegurar que el email sea el correcto
            if request.user.is_authenticated:
                quote = form.save(commit=False)
                # Mantener el email del usuario autenticado por seguridad
                quote.email = request.user.email
                quote.save()
            else:
                form.save()
            
            messages.success(request, '¡Cotización enviada exitosamente! Te contactaremos pronto.')
            return redirect('mural:mural_quote_success')
    else:
        form = MuralQuoteForm()
        # Si el usuario está autenticado, pre-llenar nombre y email
        if request.user.is_authenticated:
            form.initial['name'] = request.user.get_full_name() or request.user.username
            form.initial['email'] = request.user.email
            # Hacer el campo de email de solo lectura
            form.fields['email'].widget.attrs['readonly'] = True
    
    return render(request, 'mural/mural_quote.html', {'form': form})


def mural_quote_success(request):
    """Vista de éxito después de enviar la cotización"""
    return render(request, 'mural/mural_quote_success.html')


@login_required
def delete_mural(request, pk):
    """Elimina un mural"""
    mural = get_object_or_404(Mural, pk=pk)
    if request.method == 'POST':
        mural_title = mural.title
        mural.delete()
        messages.success(request, f'Mural "{mural_title}" eliminado exitosamente.')
        return redirect('mural:mural_list')
    return render(request, 'mural/delete_confirm.html', {
        'item': mural,
        'item_type': 'mural',
        'cancel_url': 'mural:mural_list'
    })
