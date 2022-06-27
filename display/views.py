from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from PIL import Image, ImageDraw, ImageFont


def generator(request):
    qd = request.GET
    x = min(2048, int(qd.get("x", 250)))
    y = min(2048, int(qd.get("y", 250)))
    color = qd.get("color", "192,192,192")
    color = tuple(map(int, color.split(',')))
    text = str(qd.get("text", f"{x} × {y}"))
    image = Image.new('RGB', (x, y), color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('display/fonts/SourceSansPro-Regular.ttf', size=24)
    draw.text((x/2, y/2), text, font=font, anchor="mm", fill=tuple(round(cr/2) for cr in color))
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response