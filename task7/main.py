from PIL import Image
import os

image_path = r"C:\Users\bisht\OneDrive\Desktop\internship_elevatelabs\task7\images"


output_path = r"C:\Users\bisht\OneDrive\Desktop\internship_elevatelabs\task7\resized_images"
def process_image(image_path, output_path):
    for filename in os.listdir(image_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".JPEG") or filename.endswith(".PNG") or filename.endswith(".JPG") or filename.endswith(".webp"):
            image = Image.open(os.path.join(image_path, filename))
            resized_image = image.resize((100, 100))
            resized_image.save(os.path.join(output_path, filename))
            gray_image = resized_image.convert("L")
            gray_image.save(os.path.join(output_path, f"gray_{filename}"))

process_image(image_path, output_path)