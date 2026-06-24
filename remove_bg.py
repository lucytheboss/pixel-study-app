import os
from PIL import Image

def process_image(filepath):
    img = Image.open(filepath).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Near white to transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(filepath, "PNG")

directory = "assets/"
for filename in os.listdir(directory):
    if filename.startswith("sprite_") and filename.endswith(".png"):
        process_image(os.path.join(directory, filename))
        print(f"Processed {filename}")
