from django.http import HttpResponse

from PIL import Image, ImageDraw, ImageFont

import requests, psycopg2


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
