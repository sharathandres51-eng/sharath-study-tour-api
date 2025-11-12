# 🌍 ESADE Study Tour Planner API

A simple **Flask API** that helps users plan trips by suggesting destinations, estimating costs, finding restaurants, and generating daily itineraries based on travel preferences.

## Features
- Suggest destinations by budget  
- Estimate total trip cost  
- Recommend local restaurants  
- Generate themed itineraries (food, culture, nature, nightlife)  
- Combine all into a full trip plan  


## Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/suggest-tour` | `GET` | Suggests a destination by budget |
| `/estimate-budget` | `POST` | Returns estimated total cost |
| `/find-restaurant` | `POST` | Finds a restaurant for a city |
| `/plan-trip` | `POST` | Generates a full trip plan |
| `/health` | `POST` | Returns the health status of the API |

## Setup (This can be used to replicate in an EC2 Instance as well)

```bash
git clone <repo-url>
cd <project-folder>
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install Flask
python app.py
