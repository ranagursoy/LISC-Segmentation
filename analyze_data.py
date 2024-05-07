import os
from PIL import Image

root_folder = "LISC Database"

def count_and_visualize_images(folder_path):
    image_count = 0
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".bmp"):
                image_count += 1
    return image_count

def show_single_image(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".bmp"):
                image_path = os.path.join(root, filename)
                image = Image.open(image_path)
                image.show()
                return  # Sadece ilk .bmp dosyasını göster ve işlemi sonlandır

folder_names = ["Ground Truth Segmentation", "Main Dataset", "More Dataset Without Ground Truth"]
total_count = 0
for folder_name in folder_names:
    folder_path = os.path.join(root_folder, folder_name)
    count = count_and_visualize_images(folder_path)
    show_single_image(folder_path)
    print("{}: {} .bmp file".format(folder_name, count))
    total_count += count

print("Total{} .bmp file".format(total_count))

