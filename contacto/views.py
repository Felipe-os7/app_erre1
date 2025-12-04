from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .forms import ContactForm
from .cart_utils import get_cart, get_cart_total, get_cart_summary, clear_cart
from galeria.models import Painting
from mural.models import Mural


def contacto_view(request):
	cart = get_cart(request)
	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Agregar información del carrito al mensaje
			contact_message = form.save(commit=False)
			
			# Si hay una cotización estándar en la sesión, agregarla
			standard_quote = request.session.get('standard_mural_quote')
			if standard_quote:
				contact_message.message = standard_quote + "\n\n" + contact_message.message
				del request.session['standard_mural_quote']
			
			if cart:
				cart_summary = get_cart_summary(cart)
				contact_message.message = contact_message.message + cart_summary
			contact_message.save()
			
			# Limpiar el carrito después de enviar
			clear_cart(request)
			
			messages.success(request, '¡Mensaje enviado exitosamente! Te contactaremos pronto.')
			return redirect('contacto:contacto')
	else:
		form = ContactForm()
		# Si hay una cotización estándar en la sesión, pre-llenar el mensaje
		standard_quote = request.session.get('standard_mural_quote')
		if standard_quote:
			form.initial['message'] = standard_quote
	
	cart_total = get_cart_total(cart)
	return render(request, 'contacto/contacto.html', {
		'form': form,
		'cart': cart,
		'cart_total': cart_total,
	})


def add_to_cart_view(request, item_type, item_id):
	"""Agrega un item al carrito"""
	from .cart_utils import add_to_cart
	
	if item_type == 'painting':
		item = get_object_or_404(Painting, pk=item_id)
		if not item.is_for_sale:
			return JsonResponse({'success': False, 'message': 'Esta pintura no está en venta'})
	elif item_type == 'mural':
		item = get_object_or_404(Mural, pk=item_id)
		if not item.is_for_sale:
			return JsonResponse({'success': False, 'message': 'Este mural no está en venta'})
	else:
		return JsonResponse({'success': False, 'message': 'Tipo de item inválido'})
	
	success = add_to_cart(request, item_type, item_id, item.title, item.price)
	
	if success:
		return JsonResponse({'success': True, 'message': f'{item.title} agregado al carrito'})
	else:
		return JsonResponse({'success': False, 'message': 'Este item ya está en el carrito'})


def remove_from_cart_view(request, item_type, item_id):
	"""Elimina un item del carrito"""
	from .cart_utils import remove_from_cart
	
	remove_from_cart(request, item_type, item_id)
	messages.success(request, 'Item eliminado del carrito')
	return redirect('contacto:contacto')


def clear_cart_view(request):
	"""Limpia todo el carrito"""
	clear_cart(request)
	messages.success(request, 'Carrito vaciado')
	return redirect('contacto:contacto')
