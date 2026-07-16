from generator import generate_noisy_images
from averager import average_images

if __name__ == "__main__":
    output_dir = "generated_images"

    # Step 1: Generate noisy images
    generate_noisy_images(output_dir, n_images=30)

    # Step 2: Average them to remove noise
    average_images(output_dir, output_path="denoised.png")
