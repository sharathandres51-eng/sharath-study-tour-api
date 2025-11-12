from flask import Flask, request, jsonify, render_template
from utils import destinations, restaurants, get_destination_by_budget
import random

app = Flask(__name__)


# Root route serving a simple homepage
@app.route('/')
def home_page():
    return render_template('index.html')

# Endpoint that suggests a study tour destination based on budget
@app.route('/suggest_tour')
def suggest_tour():
    try:
        budget = float(request.args.get('budget', 0))
    except ValueError:
        return jsonify({"error": "Please provide a numeric budget in euros."}), 400

    dest = get_destination_by_budget(budget)
    if not dest:
        return jsonify({"message": "Budget too low for any study tour destination."}), 200

    return jsonify({
        "budget_eur": budget,
        "suggested_destination": dest.title(),
        "message": f"With €{budget:.0f}, you can experience {dest.title()}!"
    })

# Endpoint that provides estimated budget for a given destination
@app.route('/estimate_budget')
def estimate_budget():
    dest = request.args.get('destination', '').lower()
    if dest not in destinations:
        return jsonify({"error": "Destination not supported."}), 400
    cost = destinations[dest]
    return jsonify({
        "destination": dest.title(),
        "estimated_budget_eur": cost
    })

# Endpoint that suggests a restaurant in the given destination
@app.route('/restaurant')
def restaurant():
    dest = request.args.get('destination', '').lower()
    if dest not in restaurants:
        return jsonify({"error": "Destination not supported."}), 400
    restaurant_name = random.choice(restaurants[dest])
    return jsonify({
        "destination": dest.title(),
        "recommended_restaurant": restaurant_name
    })

# Endpoint that plans a full trip based on budget, days, and preference
@app.route('/plan_trip')
def plan_trip():
    try:
        budget = float(request.args.get('budget', 0))
        days = int(request.args.get('days', 0))
        preference = request.args.get('preference', '').lower()

    except ValueError:
        return jsonify({"error": "Invalid budget or days parameter."}), 400

    if days <= 0:
        return jsonify({"error": "Days must be greater than 0."}), 400

    # Filter destinations within budget
    affordable_destinations = {
        dest: cost for dest, cost in destinations.items() if cost <= budget
    }

    if not affordable_destinations:
        return jsonify({"message": "No destination fits the budget."}), 200

    # Prioritize match based on preference weight
    selected_dest = random.choice(list(affordable_destinations.keys()))

    # Estimate cost using a formula
    daily_cost = 60  # default assumption
    estimated_total = affordable_destinations[selected_dest] + (days * daily_cost)

    # Generate sample itinerary
    itinerary = [
        f"Day {i+1}: Experience {preference} activities in {selected_dest.title()}"
        for i in range(days)
    ]

    # Pick restaurant based on destination
    restaurant_choice = random.choice(restaurants[selected_dest])

    return jsonify({
        "destination": selected_dest.title(),
        "estimated_total_cost_eur": estimated_total,
        "restaurant": restaurant_choice,
        "itinerary": itinerary,
        "message": f"Trip planned to {selected_dest.title()}!"
    })



@app.route('/health')
def health_check():
    try:
        len(destinations)  # quick sanity check
        return jsonify({
            "status": "OK",
            "message": "Study Tour API is up and running!"
        }), 200
    except Exception as e:
        # if something goes wrong internally
        return jsonify({
            "status": "ERROR",
            "message": f"Health check failed: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
