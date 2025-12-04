
from .models import SiteSetting


def social_media(request):
    """Agrega las URLs de redes sociales al contexto global"""
    setting = SiteSetting.objects.first()
    return {
        'instagram_url': setting.instagram_url if setting else '',
        'youtube_url': setting.youtube_url if setting else '',
    }

