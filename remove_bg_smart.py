import os
from PIL import Image

def process_image(filepath):
    img = Image.open(filepath).convert("RGBA")
    w, h = img.size
    pixels = img.load()
    
    # BFS to find all contiguous background pixels starting from corners
    visited = set()
    queue = [(0,0), (w-1,0), (0,h-1), (w-1,h-1)]
    
    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited: continue
        visited.add((x,y))
        
        r, g, b, a = pixels[x, y]
        # if near white
        if r > 235 and g > 235 and b > 235 and a > 0:
            pixels[x, y] = (255, 255, 255, 0)
            
            # Add neighbors
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w and 0 <= ny < h:
                    if (nx, ny) not in visited:
                        queue.append((nx, ny))
                        
    img.save(filepath, "PNG")

directory = "assets/"
for filename in os.listdir(directory):
    if filename.startswith("sprite_") and filename.endswith(".png"):
        process_image(os.path.join(directory, filename))
        print(f"Smart Processed {filename}")
