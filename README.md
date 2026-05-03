# Art Portfolio Website — Ishigaki Miyuki

A lightweight, static art portfolio website built with HTML, CSS, and vanilla JavaScript. Designed for GitHub Pages hosting. Supports English, Japanese, and Traditional Chinese.

## Quick Start

Open `index.html` in your browser to preview the site locally. No build step or server required.

Alternatively, use any local server:

```bash
python3 -m http.server 8000
# Then visit http://localhost:8000
```

## Adding Artwork

1. Add the full-size image to `images/artworks/` (recommended: ~1600px wide, JPEG or WebP)
2. Add a smaller thumbnail to `images/thumbs/` (recommended: ~600px wide)
3. Add a gallery item inside the relevant `series/series-N.html` page:

```html
<div class="gallery-item" data-title="Title" data-meta="Medium, Size, Year" data-full="images/artworks/filename.jpg">
  <img src="images/thumbs/filename.jpg" alt="Title" class="gallery-item__img" loading="lazy">
  <div class="gallery-item__overlay">
    <div>
      <p class="gallery-item__title">Title</p>
      <p class="gallery-item__meta">Medium, Year</p>
    </div>
  </div>
</div>
```

## Editing Translations

All translatable text lives in `js/translations.js`. Each entry has `en`, `ja`, and `zhTW` values. Edit the `ja` or `zhTW` values to update Japanese or Traditional Chinese text.

## File Structure

```
art-website/
├── index.html              Home page
├── video.html              YouTube video embeds
├── about.html              Artist biography
├── contact.html            Contact info and form
├── series/
│   ├── series-1.html       Artwork series pages (1-5)
│   ├── series-2.html
│   ├── series-3.html
│   ├── series-4.html
│   └── series-5.html
├── css/style.css           All styles
├── js/
│   ├── main.js             Lightbox, mobile nav, language switcher, right-click protection
│   └── translations.js     English / Japanese / Traditional Chinese translations
├── images/
│   ├── artworks/           Full-size artwork images
│   ├── thumbs/             Thumbnail versions
│   ├── originals/          Original unprocessed images
│   └── site/               Hero, portrait
├── optimize-images.py      Python script to resize and convert images
├── CNAME                   Custom domain (when ready)
└── README.md
```

## Deploying to GitHub Pages

1. Create a GitHub repository
2. Push all files to the `main` branch
3. Go to Settings → Pages → Source: "Deploy from a branch" → Branch: `main`, folder: `/ (root)`
4. Site will be live at `https://yourusername.github.io/repository-name/`

## Custom Domain

1. Buy a domain from any registrar
2. Edit the `CNAME` file with your domain name
3. Add DNS records at your registrar pointing to GitHub Pages
4. GitHub will provision HTTPS automatically

## Image Optimization Tips

- Use [Squoosh](https://squoosh.app/) to compress images
- Target ~50-80KB for thumbnails, ~200-400KB for full-size
- WebP format saves ~30% vs JPEG at same quality
- Always use `loading="lazy"` on images below the fold
- Or run `python3 optimize-images.py` to batch-process images in `images/originals/`
