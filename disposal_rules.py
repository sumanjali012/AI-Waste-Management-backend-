
'''import json
from pathlib import Path

# Load the JSON dataset
DATA_FILE = Path(__file__).with_name("disposal_data.json")


def load_disposal_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Match different names for the same waste category
CATEGORY_ALIASES = {
    "plastic bottle": "plastic",
    "plastic container": "plastic",
    "paper waste": "paper",
    "newspaper": "paper",
    "glass bottle": "glass",
    "metal can": "metal",
    "aluminium can": "metal",
    "batteries": "battery",
    "battery waste": "battery",
    "e-waste": "e_waste",
    "electronic waste": "e_waste",
    "mobile phone": "e_waste",
    "food waste": "organic",
    "food scraps": "organic",
    "general waste": "general"
}


def get_disposal_recommendation(category):

    # Check whether the input is valid
    if not isinstance(category, str) or not category.strip():
        return {
            "success": False,
            "message": "Please provide a valid waste category."
        }

    # Normalize the category
    category_key = category.strip().lower()
    category_key = CATEGORY_ALIASES.get(
        category_key,
        category_key.replace("-", "_")
    )

    # Read the dataset
    waste_data = load_disposal_data()

    # Check if the category exists
    if category_key not in waste_data:
        return {
            "success": False,
            "category": category,
            "message": (
                "Unknown waste category. Check local waste guidance "
                "before disposing of this item."
            )
        }

    # Get the matching information
    details = waste_data[category_key]

    # Return the recommendation
    return {
        "success": True,
        "category": details["display_name"],
        "waste_type": details["waste_type"],
        "recommended_action": details["recommended_action"],
        "collection_route": details["collection_route"],
        "ordinary_bin": details["ordinary_bin"],
        "special_facility_required":
            details["special_facility_required"],
        "safety": details["safety"],
        "icon": details["icon"]
    }


# Run this program directly
if __name__ == "__main__":

    category = input("Enter waste category: ")

    result = get_disposal_recommendation(category)

    print("\n--- Disposal Recommendation ---")

    for key, value in result.items():
        print(f"{key}: {value}")'''






#same code but small change

import json
from pathlib import Path

# Load the JSON dataset
DATA_FILE = Path(__file__).with_name("disposal_data.json")


def load_disposal_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Match different names for the same waste category
CATEGORY_ALIASES = {
    "plastic bottle": "plastic",
    "plastic container": "plastic",
    "paper waste": "paper",
    "newspaper": "paper",
    "glass bottle": "glass",
    "metal can": "metal",
    "aluminium can": "metal",
    "batteries": "battery",
    "battery waste": "battery",
    "e-waste": "e_waste",
    "electronic waste": "e_waste",
    "mobile phone": "e_waste",
    "food waste": "organic",
    "food scraps": "organic",
    "general waste": "general"
}


def get_disposal_recommendation(category):

    # Check if the user entered nothing
    if category is None or (
        isinstance(category, str) and not category.strip()
    ):
        return {
            "success": False,
            "category": None,
            "message": "No waste category provided. Please enter a waste type."
        }

    # Check if the input is not text
    if not isinstance(category, str):
        return {
            "success": False,
            "category": None,
            "message": "Invalid input. Please enter a waste category as text."
        }

    # Normalize the category
    category_key = category.strip().lower()
    category_key = CATEGORY_ALIASES.get(
        category_key,
        category_key.replace("-", "_")
    )

    # Load the dataset
    waste_data = load_disposal_data()

    # Check if the category exists
    if category_key not in waste_data:
        return {
            "success": False,
            "category": category.strip(),
            "message": (
                "Unknown waste category. This item was not recognized. "
                "Please enter a supported waste category."
            )
        }

    # Get the matching waste information
    details = waste_data[category_key]

    # Return disposal recommendations
    return {
        "success": True,
        "category": details["display_name"],
        "waste_type": details["waste_type"],
        "recommended_action": details["recommended_action"],
        "collection_route": details["collection_route"],
        "ordinary_bin": details["ordinary_bin"],
        "special_facility_required":
            details["special_facility_required"],
        "safety": details["safety"],
        "icon": details["icon"]
    }


# Run the program directly
if __name__ == "__main__":

    category = input("Enter waste category: ")

    result = get_disposal_recommendation(category)

    print("\n--- Disposal Recommendation ---")

    if not result["success"]:
        print(result["message"])
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
