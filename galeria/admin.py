from django.contrib import admin
from .models import Collection, Painting
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
# Submission model is kept for historical migrations but we no longer
# expose it in the admin because submissions are created directly as
# `Painting` or `mural.Mural` upon form submission.


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
	list_display = ('title',)


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'collection', 'price', 'is_for_sale', 'created_at')
	list_filter = ('category', 'collection','is_for_sale')
	search_fields = ('title', 'description', 'technique')
	fieldsets = (
		(None, {'fields': ('title', 'description', 'image', 'category', 'collection')}),
		('Detalles', {'fields': ('price', 'technique', 'dimensions', 'year', 'is_for_sale')}),
	)
	actions = [export_as_csv_action('Exportar pinturas seleccionadas')]


# Note: previous admin action to approve Submission objects (and create
# Painting/Mural instances from them) has been removed because forms now
# create `Painting` and `Mural` directly. The `Submission` model remains
# in the codebase for historical data/migrations but is intentionally not
# registered in the admin anymore.
