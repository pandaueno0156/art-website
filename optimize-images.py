"""
Image Optimization Script
Converts artwork images to optimized thumbnails and WebP format.

Requirements:
    pip install Pillow

Usage:
    1. Place original artwork images in the 'images/originals/' folder
    2. Run: python3 optimize-images.py
    3. Optimized images will be generated in images/artworks/ and images/thumbs/
"""

from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Install it with:")
    print("  pip install Pillow")
    exit(1)

ORIGINALS_DIR = Path("images/originals")
ARTWORKS_DIR = Path("images/artworks")
THUMBS_DIR = Path("images/thumbs")

FULL_SIZE_WIDTH = 1600
THUMB_WIDTH = 600
JPEG_QUALITY = 82
WEBP_QUALITY = 80

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".bmp"}


def optimize_image(input_path: Path):
    """Process a single image into full-size and thumbnail versions in both JPEG and WebP."""
    img = Image.open(input_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    stem = input_path.stem

    # Full-size version
    full_img = img.copy()
    if full_img.width > FULL_SIZE_WIDTH:
        ratio = FULL_SIZE_WIDTH / full_img.width
        full_img = full_img.resize(
            (FULL_SIZE_WIDTH, int(full_img.height * ratio)),
            Image.LANCZOS,
        )

    full_img.save(ARTWORKS_DIR / f"{stem}.jpg", "JPEG", quality=JPEG_QUALITY, optimize=True)
    full_img.save(ARTWORKS_DIR / f"{stem}.webp", "WEBP", quality=WEBP_QUALITY)

    # Thumbnail version
    thumb_img = img.copy()
    ratio = THUMB_WIDTH / thumb_img.width
    thumb_img = thumb_img.resize(
        (THUMB_WIDTH, int(thumb_img.height * ratio)),
        Image.LANCZOS,
    )

    thumb_img.save(THUMBS_DIR / f"{stem}.jpg", "JPEG", quality=JPEG_QUALITY, optimize=True)
    thumb_img.save(THUMBS_DIR / f"{stem}.webp", "WEBP", quality=WEBP_QUALITY)

    print(f"  Processed: {input_path.name} -> {stem}.jpg + {stem}.webp")


def main():
    ORIGINALS_DIR.mkdir(parents=True, exist_ok=True)
    ARTWORKS_DIR.mkdir(parents=True, exist_ok=True)
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)

    images = [
        f for f in ORIGINALS_DIR.iterdir()
        if f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not images:
        print(f"No images found in '{ORIGINALS_DIR}/'.")
        print("Place your artwork images there and run this script again.")
        return

    print(f"Found {len(images)} image(s). Optimizing...\n")

    for img_path in sorted(images):
        try:
            optimize_image(img_path)
        except Exception as e:
            print(f"  ERROR processing {img_path.name}: {e}")

    print(f"\nDone! Check '{ARTWORKS_DIR}/' and '{THUMBS_DIR}/' for results.")
    print("\nNext steps:")
    print("  1. Update gallery.html with the new image filenames")
    print("  2. Use <picture> elements for WebP with JPEG fallback (see README)")


if __name__ == "__main__":
    main()
