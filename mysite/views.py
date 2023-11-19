from django.shortcuts import render, redirect
from PIL import Image
import cv2
import numpy as np
import os
from .utils import generate_sketch, upload_to_freeimagehost
from io import BytesIO


def home_view(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]

        # Read the uploaded file into memory
        in_memory_file = BytesIO()
        for chunk in uploaded_file.chunks():
            in_memory_file.write(chunk)

        # Reset the file-like object to the beginning
        in_memory_file.seek(0)

        # Open the image using PIL from the in-memory file
        pil_image = Image.open(in_memory_file)

        # Convert PIL image to a NumPy array
        image = np.array(pil_image)

        # Generate a sketch using your own function (replace generate_sketch with your actual implementation)
        sketch = generate_sketch(photo=image)

        # Create a BytesIO object to store the sketch in memory
        sketch_in_memory = BytesIO()
        Image.fromarray(sketch).save(sketch_in_memory, format="PNG")
        sketch_in_memory.seek(0)

        # Upload the sketch to FreeImage.host and get the URL
        sketch_url = upload_to_freeimagehost(sketch_in_memory)

        # Redirect to the sketch view or any other view as needed
        return render(request, "sketch.html", {"sketch_url": sketch_url})

    return render(request, "index.html")
