#Destinations data source
destinations = {
    "bilbao": 250,
    "stgallen": 500,
    "milan": 700,
    "bangalore": 1000,
    "singapore": 1200,
    "seoul": 1500,
    "sanfrancisco": 1800
}

#Restaurants data source
restaurants = {
    "bilbao": ["La Viña del Ensanche", "Café Iruña", "Basquery"],
    "stgallen": ["Basilikum", "Netts Kafi", "Ristorante La Vigna"],
    "milan": ["Trattoria Toscana", "Luini Panzerotti", "Ratanà"],
    "bangalore": ["Toit Brewpub", "Brahmin’s Coffee Bar", "Sly Granny"],
    "singapore": ["Lau Pa Sat Hawker Centre", "Din Tai Fung", "Maxwell Food Centre"],
    "seoul": ["Gwangjang Market", "Tosokchon Samgyetang", "Onion Cafe"],
    "sanfrancisco": ["Tartine Manufactory", "Burma Love", "House of Nanking"]
}

#Function to get destination by budget
def get_destination_by_budget(budget: float):
    """Return the most suitable destination for a given budget."""
    possible = [d for d, cost in destinations.items() if cost <= budget]
    if not possible:
        return None
    return max(possible, key=lambda d: destinations[d])
