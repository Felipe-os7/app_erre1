from django.contrib import admin
from .models import Mural
import csv
from django.http import HttpResponse


def export_as_csv_action(description="Export selected objects as CSV"):
	def export_as_csv(modeladmin, request, queryset):
		meta = modeladmin.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			writer.writerow([getattr(obj, f) for f in field_names])
		return response
	export_as_csv.short_description = description
	return export_as_csv


@admin.register(Mural)
class MuralAdmin(admin.ModelAdmin):
	list_display = ('title', 'location', 'created_at')
	search_fields = ('title', 'description', 'location', 'technique')
	fieldsets = (
		(None, {'fields': ('title', 'description', 'image', 'location')}),
		('Detalles', {'fields': ('technique', 'dimensions', 'year')}),
	)
	actions = [export_as_csv_action('Exportar murales seleccionados')]
