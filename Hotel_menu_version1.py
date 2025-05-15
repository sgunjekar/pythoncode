import PIL
from PIL import ImageFont
from PIL import ImageDraw



# === SETTINGS ===
WIDTH = 900
MARGIN = 60
LINE_HEIGHT = 48
SECTION_SPACING = 50
BG_COLOR = "#f9f5f0"          # light parchment
TEXT_COLOR = "#2b463c"        # forest green
ACCENT_COLOR = "#934830"      # warm earthy red

TITLE_FONT = ImageFont.truetype("PlayfairDisplay-Regular.ttf", 60)
SUB_FONT = ImageFont.truetype("PlayfairDisplay-Regular.ttf", 28)
BODY_FONT = ImageFont.truetype("Lora-Regular.ttf", 26)

# === LOAD MENU DATA ===
with open("hotel_menu.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# === ESTIMATE HEIGHT ===
line_count = sum(3 if line.isupper() and len(line) < 30 else 1 for line in lines) + 10
HEIGHT = MARGIN * 2 + line_count * LINE_HEIGHT

# === CREATE IMAGE ===
img = PIL.Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = PIL.ImageDraw.Draw(img)
y = MARGIN

# === HEADER ===
draw.text((WIDTH // 2, y), "Skyi County Dapoli", font=TITLE_FONT, fill=TEXT_COLOR, anchor="mm")
y += LINE_HEIGHT + 20
draw.text((WIDTH // 2, y), "Where the Forest Meets the Sky", font=SUB_FONT, fill=ACCENT_COLOR, anchor="mm")
y += LINE_HEIGHT + 30

# === DRAW MENU ===
for line in lines:
    if line.isupper() and len(line) < 30:
        y += SECTION_SPACING
        draw.text((MARGIN, y), line, font=SUB_FONT, fill=ACCENT_COLOR)
        y += 10
        draw.line([(MARGIN, y), (WIDTH - MARGIN, y)], fill=ACCENT_COLOR, width=2)
        y += 20
    elif "₹" in line:
        try:
            name, price = line.rsplit("₹", 1)
            name = name.strip(". ")
            price = price.strip()
            draw.text((MARGIN + 20, y), name, font=BODY_FONT, fill=TEXT_COLOR)
            draw.text((WIDTH - MARGIN - 20, y), f"₹{price}", font=BODY_FONT, fill=TEXT_COLOR, anchor="ra")
            y += LINE_HEIGHT
        except:
            draw.text((MARGIN + 20, y), line, font=BODY_FONT, fill=TEXT_COLOR)
            y += LINE_HEIGHT
    else:
        draw.text((MARGIN + 20, y), line, font=BODY_FONT, fill=TEXT_COLOR)
        y += LINE_HEIGHT

# === FINAL TRIM ===
img = img.crop((0, 0, WIDTH, y + MARGIN))
img.save("skyi_forest_theme_menu.png")
print("✅ Forest-themed menu image saved as 'skyi_forest_theme_menu.png'")
