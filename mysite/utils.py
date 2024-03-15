import numpy as np
from PIL import Image, ImageFilter
import requests



def generate_sketch(image_array, edge_threshold=50):
    # Convert the NumPy array to a PIL Image
    original_image = Image.fromarray(image_array)

    # Convert the image to grayscale
    grayscale_image = original_image.convert('L')

    # Find edges in the image using edge detection filter
    edges = grayscale_image.filter(ImageFilter.FIND_EDGES)

    # Increase contrast of edges for more defined lines
    edges = edges.point(lambda x: 255 if x < edge_threshold else 0)

    # Optionally, invert the image if you want white lines on a black background
    # edges = ImageOps.invert(edges)

    # Convert to NumPy array if needed for further processing
    outline_array = np.array(edges)

    return outline_array


def upload_to_freeimagehost(image_data, api_key="6d207e02198a847aa98d0a2a901485a5"):
    api_url = "https://freeimage.host/api/1/upload"
    params = {
        "key": api_key,
        "action": "upload",
        "format": "json",
    }
    files = {"source": image_data}

    response = requests.post(api_url, params=params, files=files)
    data = response.json()

    if response.status_code == 200 and "image" in data:
        return data["image"]["url"]
    else:
        # Handle error, e.g., log it or return a default URL
        return "https://example.com/default-image.jpg"
