from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import CustomUserCreationForm


@require_POST
def logout_view(request):
	"""Only allow POST to logout for better security."""
	logout(request)
	return redirect('home')


def register_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, '¡Registro exitoso! Bienvenido.')
			return redirect('home')
	else:
		form = CustomUserCreationForm()
	
	return render(request, 'registration/register.html', {'form': form})
