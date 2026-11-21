"""Agrega el logo oficial de Odoo (versión blanca) sobre una placa morada #714B67
en la esquina superior izquierda de una portada 1200x630.
Uso: python3 aplicar_logo.py entrada.jpg salida.jpg
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

LOGO = Path(__file__).with_name("odoo-logo-white.png")
W, H = 1200, 630
LOGO_W, MARGIN, PAD, RADIUS = 170, 36, 18, 16
PURPLE = (113, 75, 103, 235)  # #714B67

def portada(src, dst):
    im = Image.open(src).convert("RGB")
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    l, t = (im.width - W) // 2, (im.height - H) // 2
    im = im.crop((l, t, l + W, t + H)).convert("RGBA")
    logo = Image.open(LOGO).convert("RGBA")
    lh = round(logo.height * LOGO_W / logo.width)
    logo = logo.resize((LOGO_W, lh), Image.LANCZOS)  # solo escala, sin alterar colores ni proporciones
    badge = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(badge).rounded_rectangle(
        [MARGIN, MARGIN, MARGIN + LOGO_W + 2 * PAD, MARGIN + lh + 2 * PAD], RADIUS, fill=PURPLE)
    im.alpha_composite(badge)
    im.alpha_composite(logo, (MARGIN + PAD, MARGIN + PAD))
    im.convert("RGB").save(dst, quality=85, optimize=True)

if __name__ == "__main__":
    portada(sys.argv[1], sys.argv[2])
