document.addEventListener('DOMContentLoaded', function(){
  const overlay = document.createElement('div');
  overlay.className = 'lightbox-overlay';
  overlay.tabIndex = -1;
  overlay.innerHTML = '<button class="lb-prev" aria-label="Anterior">‹</button><img src="" alt=""><button class="lb-next" aria-label="Siguiente">›</button><div class="lb-counter"></div>';
  document.body.appendChild(overlay);

  const imgEl = overlay.querySelector('img');
  const prevBtn = overlay.querySelector('.lb-prev');
  const nextBtn = overlay.querySelector('.lb-next');
  const counter = overlay.querySelector('.lb-counter');

  const links = Array.from(document.querySelectorAll('a.lightbox'));
  function showByIndex(i){
    if(i < 0 || i >= links.length) return;
    const url = links[i].getAttribute('href');
    imgEl.src = url;
    overlay.classList.add('show');
    overlay.dataset.index = i;
    counter.textContent = (i+1) + ' / ' + links.length;
  }

  function hide(){
    overlay.classList.remove('show');
    imgEl.src = '';
    delete overlay.dataset.index;
  }

  function showNext(){
    const idx = Number(overlay.dataset.index || 0);
    const next = (idx + 1) % links.length;
    showByIndex(next);
  }
  function showPrev(){
    const idx = Number(overlay.dataset.index || 0);
    const prev = (idx - 1 + links.length) % links.length;
    showByIndex(prev);
  }

  overlay.addEventListener('click', function(e){
    if(e.target === overlay) hide();
  });
  prevBtn.addEventListener('click', function(e){ e.stopPropagation(); showPrev(); });
  nextBtn.addEventListener('click', function(e){ e.stopPropagation(); showNext(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') hide(); if(e.key === 'ArrowRight') showNext(); if(e.key === 'ArrowLeft') showPrev(); });

  links.forEach(function(a, i){
    a.addEventListener('click', function(e){
      e.preventDefault();
      showByIndex(i);
    });
  });
});
