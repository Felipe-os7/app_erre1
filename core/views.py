from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from galeria.models import Painting
from mural.models import Mural
from .models import SiteSetting, News
from .forms import NewsForm


def _make_embed_url(url: str) -> str:
	if not url:
		return ''
	if 'watch?v=' in url:
		return url.replace('watch?v=', 'embed/')
	if 'youtu.be/' in url:
		return url.replace('youtu.be/', 'www.youtube.com/embed/')
	return url


def home(request):
	# Featured painting: use setting if present, otherwise latest
	setting = SiteSetting.objects.first()
	featured = None
	artist_bio = ''
	video_embed = ''
	instagram_url = ''
	youtube_url = ''
	if setting:
		artist_bio = setting.artist_bio
		video_embed = _make_embed_url(setting.featured_video_url)
		instagram_url = setting.instagram_url
		youtube_url = setting.youtube_url
		if setting.featured_painting:
			featured = setting.featured_painting

	if not featured:
		featured = Painting.objects.order_by('-created_at').first()

	latest_paintings = Painting.objects.order_by('-created_at')[:6]
	latest_murals = Mural.objects.order_by('-created_at')[:6]
	news = News.objects.order_by('-created_at')[:10]

	return render(request, 'home.html', {
		'featured': featured,
		'artist_bio': artist_bio,
		'video_embed': video_embed,
		'instagram_url': instagram_url,
		'youtube_url': youtube_url,
		'latest_paintings': latest_paintings,
		'latest_murals': latest_murals,
		'news': news,
	})


@login_required
def news_submit(request):
	"""Form to submit a news item with optional image. Requires login."""
	if request.method == 'POST':
		form = NewsForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:news_submit_success')
	else:
		form = NewsForm()
	return render(request, 'core/news_submit.html', {'form': form})


def news_submit_success(request):
	return render(request, 'core/news_submit_success.html')


@login_required
def delete_news(request, pk):
    """Elimina una noticia"""
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news_title = news.title
        news.delete()
        messages.success(request, f'Noticia "{news_title}" eliminada exitosamente.')
        return redirect('home')
    return render(request, 'core/delete_confirm.html', {
        'item': news,
        'item_type': 'noticia',
        'cancel_url': 'home'
    })
