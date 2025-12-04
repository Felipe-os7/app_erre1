document.addEventListener('DOMContentLoaded', function () {
  const carousels = document.querySelectorAll('.static-carousel');
  carousels.forEach((c) => {
    // Only consider direct child images (ignore indicators span elements)
    const imgs = Array.from(c.querySelectorAll(':scope > img'));
    if (!imgs.length) return;
    let idx = imgs.findIndex(i => i.classList.contains('active'));
    if (idx === -1) idx = 0;
    const interval = parseInt(c.getAttribute('data-interval') || '3000', 10);

    // find or create indicators
    let indicators = Array.from(c.querySelectorAll('.carousel-indicators .indicator'));
    const indicatorsContainer = c.querySelector('.carousel-indicators');
    if (!indicators.length && indicatorsContainer) {
      // create indicators based on number of imgs
      for (let i = 0; i < imgs.length; i++) {
        const span = document.createElement('span');
        span.className = 'indicator' + (i === idx ? ' active' : '');
        span.setAttribute('data-index', String(i));
        indicatorsContainer.appendChild(span);
      }
      indicators = Array.from(c.querySelectorAll('.carousel-indicators .indicator'));
    }

    function showSlide(i) {
      if (i === idx) return;
      imgs[idx].classList.remove('active');
      if (indicators[idx]) indicators[idx].classList.remove('active');
      idx = i % imgs.length;
      imgs[idx].classList.add('active');
      if (indicators[idx]) indicators[idx].classList.add('active');
    }

    let timer = setInterval(() => {
      const next = (idx + 1) % imgs.length;
      showSlide(next);
    }, interval);

    // click on indicators
    indicators.forEach((dot) => {
      dot.addEventListener('click', (e) => {
        const i = parseInt(dot.getAttribute('data-index'), 10);
        if (Number.isFinite(i)) {
          clearInterval(timer);
          showSlide(i);
          // restart timer
          timer = setInterval(() => {
            const next = (idx + 1) % imgs.length;
            showSlide(next);
          }, interval);
        }
      });
    });

    // pause on hover
    c.addEventListener('mouseenter', () => clearInterval(timer));
    c.addEventListener('mouseleave', () => {
      clearInterval(timer);
      timer = setInterval(() => {
        const next = (idx + 1) % imgs.length;
        showSlide(next);
      }, interval);
    });
  });
});
