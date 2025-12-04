from django.core.files import File

from galeria.models import Collection, Painting
from mural.models import Mural


def run():
    # Create a sample collection
    col, created = Collection.objects.get_or_create(
        title='Colección de ejemplo',
        defaults={'description': 'Colección de ejemplo generada automáticamente.'}
    )

    # Create sample painting
    painting, p_created = Painting.objects.get_or_create(
        title='Pintura de ejemplo',
        defaults={
            'description': 'Una pintura de ejemplo añadida por el script.',
            'collection': col,
            'price': 120.00,
            'technique': 'Óleo sobre lienzo',
            'dimensions': '50x70 cm',
            'year': 2022,
            'is_for_sale': True,
        }
    )
    try:
        if not painting.image:
            with open('media/paintings/sample_painting.png', 'rb') as f:
                painting.image.save('sample_painting.png', File(f), save=True)
    except FileNotFoundError:
        print('Advertencia: media/paintings/sample_painting.png no encontrada; omitiendo imagen de la pintura.')

    # Create sample mural
    mural, m_created = Mural.objects.get_or_create(
        title='Mural de ejemplo',
        defaults={
            'description': 'Un mural de ejemplo generado automáticamente.',
            'location': 'Centro ciudad',
            'price': 800.00,
            'technique': 'Spray y acrílico',
            'dimensions': '500x300 cm',
            'year': 2021,
            'is_for_sale': False,
        }
    )
    try:
        if not mural.image:
            with open('media/murals/sample_mural.png', 'rb') as f:
                mural.image.save('sample_mural.png', File(f), save=True)
    except FileNotFoundError:
        print('Advertencia: media/murals/sample_mural.png no encontrada; omitiendo imagen del mural.')

    print('Hecho. Created painting id:', painting.pk, 'mural id:', mural.pk)


if __name__ == '__main__':
    run()
