from PIL import Image, ImageDraw, ImageFont

# === Settings ===
WIDTH = 600
HEIGHT = 200
BG_COLOR = "#fdf6ec"
TEXT_COLOR = "#2b463c"
SHADOW_COLOR = "#888888"
PRICE_COLOR = "#934830"
ACCENT_COLOR = "#0f3d30"

# === Load Assets ===
dish_name = "Prawns Masala"
price = "₹450"
description = "Traditional coastal spice magic!"
icon_path = "prawns.png"  # or use any small PNG

# === Fonts ===
TITLE_FONT = ImageFont.truetype("PlayfairDisplay-Regular.ttf", 36)
PRICE_FONT = ImageFont.truetype("PlayfairDisplay-Regular.ttf", 28)
DESC_FONT = ImageFont.truetype("Lora-Regular.ttf", 20)

# === Create Canvas ===
img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# === Icon ===
if icon_path:
    icon = Image.open(icon_path).convert("RGBA").resize((64, 64))
    img.paste(icon, (30, 50), icon)

# === Dish Name with Shadow ===
x_text = 110
y_text = 50
draw.text((x_text + 2, y_text + 2), dish_name, font=TITLE_FONT, fill=SHADOW_COLOR)  # shadow
draw.text((x_text, y_text), dish_name, font=TITLE_FONT, fill=TEXT_COLOR)

# === Price ===
draw.text((WIDTH - 110, y_text + 8), price, font=PRICE_FONT, fill=PRICE_COLOR)

# === Description ===
draw.text((x_text, y_text + 50), description, font=DESC_FONT, fill=ACCENT_COLOR)

# === Save Image ===
img.save("label_prawns_masala.png")
print("✅ Stylish dish label saved!")
