
from transformers import pipeline

print("Loading AI model... Please wait.")

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

image_path = input("Enter the full path of your image: ").strip().strip('"')

print("\nAnalyzing image...")

results = classifier(image_path)

print("\nAI Predictions:")

for result in results[:5]:
    print(
        "Label:", result["label"],
        "| Confidence:", round(result["score"] * 100, 2), "%"
    )
