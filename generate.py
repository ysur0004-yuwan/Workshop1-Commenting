import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def generate_noisy_images(
    output_dir: str,
    n_images: int = 20,
    width: int = 800,
    height: int = 400,
    noise_level: float = 0.25
):
    """
    Generate noisy images containing the text 'MMA3001'.

    Parameters
    ----------
    output_dir : str
        Directory to save generated images.
    n_images : int
        Number of images to generate.
    width : int
        Image width in pixels.
    height : int
        Image height in pixels.
    noise_level : float
        Strength of random noise added to the image.
    """

    os.makedirs(output_dir, exist_ok=True)

    # Try to load a default font; fallback if unavailable
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()

    for i in range(n_images):
        # Base white background
        img = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(img)

        # Center text
        text = "MMA3001"
        text_w, text_h = draw.textsize(text, font=font)
        pos = ((width - text_w) // 2, (height - text_h) // 2)

        draw.text(pos, text, fill="black", font=font)

        # Add random noise
        noise = np.random.randn(height, width, 3) * 255 * noise_level
        noisy = np.clip(np.array(img) + noise, 0, 255).astype(np.uint8)

        noisy_img = Image.fromarray(noisy)
        noisy_img.save(os.path.join(output_dir, f"noisy_{i:03d}.png"))

    print(f"Generated {n_images} noisy images in {output_dir}")
