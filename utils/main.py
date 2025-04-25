from PIL import Image
import os
import random
import requests
from io import BytesIO
import json

os.makedirs("output", exist_ok=True)

canvas_width = 300
canvas_height = 300

with open('assets.json', 'r') as f:
    assets = json.load(f)

def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    return img

bg_url = random.choice(assets["bg"])
sword_url = random.choice(assets["sword"])
cloth_url = random.choice(assets["cloth"])
face_url = random.choice(assets["face"])
horn_url = random.choice(assets["horn"])
eyes_url = random.choice(assets["eyes"])
middle_url = random.choice(assets["middle"])

bg_image = download_image(bg_url)
sword_image = download_image(sword_url)
cloth_image = download_image(cloth_url)
face_image = download_image(face_url)
horn_image = download_image(horn_url)
eyes_image = download_image(eyes_url)
middle_image = download_image(middle_url)

base_canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
face_canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

def draw_body(base):
    resized_bg = bg_image.resize((canvas_width, canvas_height))
    base.paste(resized_bg, (0, 0), resized_bg)

    sword_resized = sword_image.resize((int(sword_image.width * 1.2), int(sword_image.height * 1.2)))
    base.paste(sword_resized, (int((canvas_width - sword_resized.width) / 2) + 15, 30), sword_resized)

    cloth_resized = cloth_image.resize((int(cloth_image.width * 1.2), int(cloth_image.height * 1.2)))
    base.paste(cloth_resized, (int((canvas_width - cloth_resized.width) / 2), 110), cloth_resized)

def draw_face(face_layer):
    base_x = int((canvas_width - cloth_image.width) / 2)

    face_resized = face_image.resize((int(face_image.width * 0.5), int(face_image.height * 0.5)))
    face_layer.paste(face_resized, (base_x + 16, 43), face_resized)

    horn_resized = horn_image.resize((int(horn_image.width * 0.5), int(horn_image.height * 0.5)))
    face_layer.paste(horn_resized, (base_x + 16, 10), horn_resized)

    eyes_resized = eyes_image.resize((int(eyes_image.width * 0.4), int(eyes_image.height * 0.4)))
    face_layer.paste(eyes_resized, (base_x + 28, 70), eyes_resized)

    middle_resized = middle_image.resize((int(middle_image.width * 0.4), int(middle_image.height * 0.4)))
    face_layer.paste(middle_resized, (base_x + 30, 108), middle_resized)

draw_body(base_canvas)
draw_face(face_canvas)

final_image = Image.alpha_composite(base_canvas, face_canvas)

final_image.save("../output/combined.png")

print("Images saved to output folder.")

