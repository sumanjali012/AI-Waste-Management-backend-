# Waste Disposal Recommendation Module

## Project Description
This module provides appropriate waste disposal instructions based on the waste category entered by the user.

It is part of an AI-powered waste management web application that aims to promote safe waste disposal and reduce environmental pollution.

## Features
- Identifies disposal guidance using a waste category.
- Provides recommended disposal actions.
- Indicates whether ordinary-bin disposal is appropriate.
- Identifies when a special collection facility is required.
- Provides safety precautions for hazardous waste.
- Handles unknown and empty categories.

## Technologies Used
- Python
- JSON
- unittest

## Files
- `disposal_rules.py` — Contains the disposal recommendation logic.
- `disposal_data.json` — Stores waste categories and disposal instructions.
- `test_disposal.py` — Contains automated tests.
- `README.md` — Documents this module.

## How to Run
Open the terminal in this folder and execute:

```bash
python disposal_rules.py
```

Enter a waste category when prompted.

## How to Run Tests
Execute:

```bash
python -m unittest -v test_disposal.py
```

## Example Categories
- Battery
- Plastic Bottle
- Paper
- Glass Bottle
- E-Waste
- Food Waste

## Safety Note
Hazardous waste, batteries, and electronic waste should be handled according to local disposal guidelines. Do not dismantle, crush, or burn batteries or electronic devices.

## Future Integration
This module can be connected to a web application backend so that disposal instructions can be displayed after the AI model identifies waste from an uploaded image.
