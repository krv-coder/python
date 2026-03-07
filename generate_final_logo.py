import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_modern_dev_logo():
    # 1. Setup Canvas
    size = (1000, 1000)
    bg_color = (13, 17, 23)  # GitHub Dark Theme Grey
    accent_color = (88, 166, 255) # Soft Blue Neon
    secondary_color = (210, 100, 255) # Purple Flare
    
    img = Image.new('RGBA', size, bg_color)
    overlay = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 2. Draw 3D Perspective Grid (Darkened)
    grid_y = 700
    grid_color_dark = (40, 60, 100, 40) # Very subtle dark blue
    for i in range(0, 20):
        # Horizontal lines with lower alpha for "dark" look
        alpha = int(80 * (i / 20))
        y = grid_y + (i**2.2) * 0.5
        if y < 1000:
            draw.line([(0, y), (1000, y)], fill=(88, 166, 255, alpha), width=2)
    
    # Vanishing points for vertical grid lines (darker)
    for x in range(-500, 1500, 80):
        draw.line([(500, grid_y - 100), (x, 1000)], fill=(88, 166, 255, 30), width=2)

    # 3. Create the Terminal Window Icon
    win_w, win_h = 500, 320
    win_x, win_y = (1000 - win_w) // 2, 300
    
    # Window Shadow/Glow (Enhanced Glow)
    for i in range(30, 0, -3):
        draw.rounded_rectangle([win_x-i, win_y-i, win_x+win_w+i, win_y+win_h+i], 
                               radius=15, outline=(88, 166, 255, 20), width=2)

    # Window Body
    draw.rounded_rectangle([win_x, win_y, win_x+win_w, win_y+win_h], 
                           radius=12, fill=(20, 20, 35, 240), outline=accent_color, width=3)
    
    # Title Bar
    draw.line([(win_x, win_y+40), (win_x+win_w, win_y+40)], fill=accent_color, width=2)
    # Window Buttons (Red, Yellow, Green)
    for i, color in enumerate([(255, 95, 87), (255, 189, 46), (39, 201, 63)]):
        bx = win_x + 20 + (i * 25)
        draw.ellipse([bx, win_y + 12, bx + 12, win_y + 24], fill=color)

    # 4. Coding Symbols (>_)
    try:
        font_code = ImageFont.truetype("consola.ttf", 120)
        font_text = ImageFont.truetype("arialbd.ttf", 80)
    except:
        font_code = font_text = ImageFont.load_default()

    # Draw "> _" with a flicker effect
    t_draw = ImageDraw.Draw(overlay)
    t_draw.text((win_x + 60, win_y + 100), ">", font=font_code, fill=accent_color)
    t_draw.rectangle([win_x + 150, win_y + 195, win_x + 230, win_y + 205], fill=secondary_color)


    
    # Apply Heavier Blur for Enhanced Neon Glow Effect
    glow_layer = overlay.filter(ImageFilter.GaussianBlur(radius=6))
    final_img = Image.alpha_composite(img, glow_layer)
    final_img = Image.alpha_composite(final_img, overlay)

    # 6. Save
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    output_path = os.path.join(desktop, "modern_coding_club_logo.png")
    final_img.convert("RGB").save(output_path)
    print(f"Professional Logo saved to: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    create_modern_dev_logo()