import os
from django.core.files import File
from random import choice, randint
from galeria.models import Collection, Painting
from mural.models import Mural

PAINTING_IMAGE = 'media/paintings/sample_painting.png'
MURAL_IMAGE = 'media/murals/sample_mural.png'

def run(num_paintings=5, num_murals=3):
    col, _ = Collection.objects.get_or_create(title='Colección masiva', defaults={'description':'Colección generada en lote.'})

    techniques = ['Óleo sobre lienzo','Acrílico','Acuarela','Mixta','Spray']

    for i in range(num_paintings):
        title = f'Pintura ejemplo {i+1}'
        p, created = Painting.objects.get_or_create(title=title, defaults={
            'description': 'Descripción de muestra para la pintura '+title,
            'collection': col,
            'price': round(randint(50,1200) + randint(0,99)/100,2),
            'technique': choice(techniques),
            'dimensions': f'{randint(30,120)}x{randint(30,120)} cm',
            'year': randint(2000,2025),
            'is_for_sale': choice([True, False]),
        })
        if p and (not p.image) and os.path.exists(PAINTING_IMAGE):
            with open(PAINTING_IMAGE,'rb') as f:
                p.image.save(f'bulk_painting_{i+1}.png', File(f), save=True)

    for j in range(num_murals):
        title = f'Mural ejemplo {j+1}'
        m, created = Mural.objects.get_or_create(title=title, defaults={
            'description': 'Descripción de muestra para el mural '+title,
            'location': 'Ubicación '+str(j+1),
            'price': round(randint(300,5000) + randint(0,99)/100,2),
            'technique': choice(techniques),
            'dimensions': f'{randint(200,800)}x{randint(150,600)} cm',
            'year': randint(2000,2025),
            'is_for_sale': choice([True, False]),
        })
        if m and (not m.image) and os.path.exists(MURAL_IMAGE):
            with open(MURAL_IMAGE,'rb') as f:
                m.image.save(f'bulk_mural_{j+1}.png', File(f), save=True)

    print('Se crearon', num_paintings, 'pinturas y', num_murals, 'murales de ejemplo.')

if __name__ == '__main__':
    import os
    run()
