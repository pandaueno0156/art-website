document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initLightbox();
  initFilterTabs();
});

/* ===== Mobile Navigation Toggle ===== */
function initMobileNav() {
  const toggle = document.querySelector('.nav__toggle');
  const links = document.querySelector('.nav__links');

  if (!toggle || !links) return;

  toggle.addEventListener('click', () => {
    toggle.classList.toggle('active');
    links.classList.toggle('active');
  });

  document.querySelectorAll('.nav__link').forEach(link => {
    link.addEventListener('click', () => {
      toggle.classList.remove('active');
      links.classList.remove('active');
    });
  });
}

/* ===== Lightbox ===== */
function initLightbox() {
  const lightbox = document.querySelector('.lightbox');
  if (!lightbox) return;

  const lightboxImg = lightbox.querySelector('.lightbox__img');
  const lightboxTitle = lightbox.querySelector('.lightbox__title');
  const lightboxMeta = lightbox.querySelector('.lightbox__meta');
  const closeBtn = lightbox.querySelector('.lightbox__close');

  document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', () => {
      const imgSrc = item.dataset.full || item.querySelector('img').src;
      const title = item.dataset.title || '';
      const meta = item.dataset.meta || '';

      lightboxImg.src = imgSrc;
      lightboxImg.alt = title;
      lightboxTitle.textContent = title;
      lightboxMeta.textContent = meta;
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });
}

/* ===== Gallery Filter Tabs ===== */
function initFilterTabs() {
  const tabs = document.querySelectorAll('.filter-tab');
  const items = document.querySelectorAll('.gallery-item');

  if (!tabs.length || !items.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const category = tab.dataset.category;

      items.forEach(item => {
        if (category === 'all' || item.dataset.category === category) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}
