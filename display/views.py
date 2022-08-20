from django.http import HttpResponse

from PIL import Image, ImageDraw, ImageFont

import requests, psycopg2

def unpack(string):
    s = string
    s.replace("7", "66").replace("6", "55").replace("5", "44").replace("4", "33").replace("3", "22").replace("2", "11").replace("1", "00").replace("0", "dd")
    return s

def generator(request):
    qd = request.GET
    x = min(2048, int(qd.get("x", 250)))
    y = min(2048, int(qd.get("y", 250)))
    color = qd.get("color", "192,192,192")
    color = tuple(map(int, color.split(',')))
    text = str(qd.get("text", f"{x} × {y}"))
    font = str(qd.get("font", "serif"))
    image = Image.new('RGB', (x, y), color)
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype(f'display/fonts/{font}/Regular.ttf', size=min(120, max(12, int(qd.get("fontsize", 24)))))
    except:
        font = ImageFont.truetype('display/fonts/serif/Regular.ttf', size=min(120, max(12, int(qd.get("fontsize", 24)))))
    draw.multiline_text((x/2, y/2), text, font=font, anchor="mm", fill=tuple(round(cr/2) for cr in color))
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response

def place(request):
    image = Image.new('RGB', (64, 64), 0xE6E7E8)
    qd = request.GET
    encodedinfo = unpack(qd.get('info', "7777777777777777"))
    encodedlist = list(encodedinfo)
    colorlist = []
    convdict = {
        "a": 0x31373D,
        "b": 0x585954,
        "c": 0xB3B1AB,
        "d": 0xE6E7E8,
        "e": 0xFF83F8,
        "f": 0xF63E06,
        "g": 0xF4900C,
        "h": 0xC1694F,
        "i": 0xFDCB58,
        "j": 0xBCDB38,
        "k": 0x78B159,
        "l": 0x0DDBD0,
        "m": 0x55ACEE,
        "n": 0x0C2ED2,
        "o": 0xAA8ED6,
        "p": 0x801D6C
    }
    for point in encodedlist:
        colorlist.append(convdict["point"])
    return str(colorlist)
    