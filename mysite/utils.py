import cv2
import requests


def generate_sketch(photo):
    grey_image = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

    inverted_image = cv2.bitwise_not(grey_image)

    blurred_image = cv2.GaussianBlur(inverted_image, (55, 55), 0)

    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    sketch = cv2.divide(grey_image, inverted_blurred_image, scale=256.0)

    return sketch


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
