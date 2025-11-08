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

if __name__ == '__main__':
    app.run(debug=True)
