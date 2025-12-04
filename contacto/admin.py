from django.contrib import admin
from .models import ContactMessage, MuralQuote


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'created_at')
	search_fields = ('name', 'email', 'message')
	readonly_fields = ('created_at',)


@admin.register(MuralQuote)
class MuralQuoteAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'technique', 'dimensions', 'created_at')
	search_fields = ('name', 'email', 'technique', 'dimensions', 'message')
	readonly_fields = ('created_at',)
	list_filter = ('created_at',)
	fieldsets = (
		('Información de Contacto', {
			'fields': ('name', 'email')
		}),
		('Detalles del Proyecto', {
			'fields': ('technique', 'dimensions', 'message')
		}),
		('Información del Sistema', {
			'fields': ('created_at',),
			'classes': ('collapse',)
		}),
	)
