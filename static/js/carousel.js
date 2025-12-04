// Simple news carousel: cycles .news-item elements by toggling 'active'
document.addEventListener('DOMContentLoaded', function () {
  const items = Array.from(document.querySelectorAll('.news-item'));
  if (!items.length) return;
  let idx = items.findIndex(i => i.classList.contains('active'));
  if (idx === -1) idx = 0;
  const ROTATE_MS = 10000;
  let timer = null;

  function showSlide(i) {
    items[idx].classList.remove('active');
    idx = (i + items.length) % items.length;
    items[idx].classList.add('active');
  }

  function startTimer() {
    stopTimer();
    timer = setInterval(() => {
      showSlide(idx + 1);
    }, ROTATE_MS);
  }

  function stopTimer() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  // start rotation
  startTimer();

  // prev/next controls (if present)
  const prevBtn = document.querySelector('.news-prev');
  const nextBtn = document.querySelector('.news-next');
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      stopTimer();
      showSlide(idx - 1);
      startTimer();
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      stopTimer();
      showSlide(idx + 1);
      startTimer();
    });
  }
});
