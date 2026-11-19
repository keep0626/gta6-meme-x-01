#!/usr/bin/env python3
"""Build the GTA 6 x make.fun meme (1024x1024 PNG).

Vice City sunset gradient, the joke in big type, make.fun's ghost mascot
worked into the scene, and the make.fun pitch in the bottom banner.
Deterministic, offline: PIL + DejaVu fonts + the press-kit ghost only.
"""
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load_font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def sunset():
    top = (46, 16, 101)
    mid = (190, 24, 93)
    bot = (249, 115, 22)
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        if y < H // 2:
            c = lerp(top, mid, y / (H // 2))
        else:
            c = lerp(mid, bot, (y - H // 2) / (H // 2))
        for x in range(W):
            px[x, y] = c
    return img


def text_center(draw, y, s, font, fill, stroke=3, stroke_fill=(20, 8, 40)):
    draw.text((W // 2, y), s, font=font, fill=fill, anchor="ma",
              stroke_width=stroke, stroke_fill=stroke_fill)


def main():
    img = sunset()
    d = ImageDraw.Draw(img)
    # low sun over the Vice City horizon
    d.ellipse([W // 2 - 130, 300, W // 2 + 130, 560], fill=(255, 214, 120))
    d.ellipse([W // 2 - 130, 300, W // 2 + 130, 560], outline=(255, 170, 60), width=6)
    # horizon line
    d.rectangle([0, 560, W, 566], fill=(30, 10, 50))

    big = load_font("DejaVuSans-Bold.ttf", 92)
    med = load_font("DejaVuSans-Bold.ttf", 54)
    small = load_font("DejaVuSans-Bold.ttf", 34)
    tiny = load_font("DejaVuSans-Bold.ttf", 28)

    text_center(d, 60, "13 YEARS.", big, (255, 255, 255))
    text_center(d, 170, "GTA 6 IS FINALLY HERE.", med, (255, 214, 120))

    # the ghost, cruising into Vice City on the sunset
    ghost = Image.open(os.path.join(HERE, "ghost.png")).convert("RGBA")
    ghost = ghost.resize((340, 340), Image.LANCZOS)
    img.paste(ghost, ((W - 340) // 2, 530), ghost)
    d = ImageDraw.Draw(img)

    # bottom banner with the pitch
    d.rectangle([0, 880, W, H], fill=(20, 8, 40))
    text_center(d, 896, "While you waited, my AI agent", small, (255, 255, 255), stroke=0)
    text_center(d, 938, "earned real money on make.fun", small, (255, 214, 120), stroke=0)
    d.text((28, 20), "VICE CITY", font=tiny, fill=(255, 255, 255))
    d.text((W - 28, 20), "EST. 2013", font=tiny, fill=(255, 255, 255), anchor="ra")

    out = os.path.join(HERE, "meme.png")
    img.save(out, "PNG", optimize=True)
    print(out, os.path.getsize(out), img.size)


if __name__ == "__main__":
    main()
