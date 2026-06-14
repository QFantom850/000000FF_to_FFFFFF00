from pathlib import Path
from PIL import Image


img_path = Path(input("image path: "))
inverse_mode = input("use inverted mode? (y/n): ").lower() == "y"

with Image.open(img_path) as img:
    
    img = img.convert("L")
    new_img = Image.new("RGBA", img.size)
    base_color = 0 if inverse_mode else 255

    for x in range(img.width):
        for y in range(img.height):
    
            brightness = img.getpixel((x, y))
            alpha = (255 - brightness) if inverse_mode else brightness

            new_img.putpixel((x, y), (base_color, base_color, base_color, alpha))

    new_img.save("output.png")
    print("background removed successfully")