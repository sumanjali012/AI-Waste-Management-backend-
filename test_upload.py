
import requests

image_path = input("Enter the full path of your image: ")

try:
    with open(image_path, "rb") as image_file:
        response = requests.post(
            "http://127.0.0.1:5000/api/upload",
            files={"image": image_file}
        )

    print("\nServer response:")
    print(response.status_code)
    print(response.json())

except FileNotFoundError:
    print("Error: Image file not found. Check the path.")

except requests.exceptions.ConnectionError:
    print("Error: Flask server is not running.")

