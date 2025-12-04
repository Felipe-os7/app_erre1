from django.contrib import admin
from .models import SiteSetting, News
from django.utils.html import format_html


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
	list_display = ('__str__',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'image_tag')
	list_display_links = ('title',)
	readonly_fields = ('image_tag',)

	def image_tag(self, obj):
		if obj.image:
			return format_html('<img src="{}" style="max-height:60px;" />', obj.image.url)
		return ''
	image_tag.short_description = 'Imagen'
