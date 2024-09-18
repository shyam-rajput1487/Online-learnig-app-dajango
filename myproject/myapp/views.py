# views.py

from django.http import HttpResponse
from django.shortcuts import render
import requests
import io
from PIL import Image

# Define your view functions here

def homepage(request):
    return render(request, "index.html")

API_URL = "https://api-inference.huggingface.co/models/Melonie/text_to_image_finetuned"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad response status
        return response.content
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def generate_image(text_input):
    if text_input:
        try:
            image_bytes = query({"inputs": text_input})
            if image_bytes:
                image = Image.open(io.BytesIO(image_bytes))
                return image
            else:
                print("Failed to generate image. Invalid image data received.")
        except OSError as e:
            print("Error creating image:", e)
    else:
        print("Please provide some text input.")
