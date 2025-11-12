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

restaurants = {
    "bilbao": ["La Viña del Ensanche", "Nerua", "Asador Indusi"],
    "stgallen": ["Einstein Gourmet", "Netts Schützengarten", "Marktplatz"],
    "milan": ["Luini Panzerotti", "Nobu Milano", "Trattoria Milanese"],
    "bangalore": ["MTR", "Toit", "Vidyarthi Bhavan"],
    "singapore": ["Hawker Chan", "Jumbo Seafood", "Din Tai Fung"],
    "seoul": ["Myeongdong Kyoja", "Gwangjang Market", "Jungsik"],
    "sanfrancisco": ["Tartine Bakery", "The Slanted Door", "House of Prime Rib"]
}

#User preferences data source
preferences = {
    "bilbao": {
        "food": ["pintxos crawl", "local seafood tour", "Basque cooking workshop"],
        "culture": ["Guggenheim museum visit", "art district walk", "Basque history tour"],
        "nature": ["coastal hiking", "mountain viewpoint tour", "botanical gardens"],
        "nightlife": ["Casco Viejo bar hopping", "cocktail lounges", "live jazz clubs"]
    },
    "stgallen": {
        "food": ["Swiss chocolate tasting", "cheese fondue dining", "local brewery tour"],
        "culture": ["Abbey library visit", "Swiss heritage museum", "old town walk"],
        "nature": ["Alpine day trip", "lake picnic", "scenic train ride"],
        "nightlife": ["Altstadt bars", "local beer pubs", "underground clubs"]
    },
    "milan": {
        "food": ["pasta masterclass", "gelato tour", "espresso tasting"],
        "culture": ["Duomo rooftop visit", "Leonardo museum", "opera night"],
        "nature": ["Lake Como day-trip", "garden district walk", "canal stroll"],
        "nightlife": ["Navigli bars", "electronic clubs", "wine lounges"]
    },
    "bangalore": {
        "food": ["South Indian breakfast trail", "biriyani hotspots", "filter coffee tour"],
        "culture": ["heritage walk", "silk weaving center", "local markets"],
        "nature": ["Nandi Hills sunrise", "botanical gardens", "lakeside walk"],
        "nightlife": ["Indiranagar pubs", "microbreweries", "live music bars"]
    },
    "singapore": {
        "food": ["hawker center tour", "michelin street food", "Asian fusion dining"],
        "culture": ["Marina Bay tour", "temple walk", "art science museum"],
        "nature": ["Gardens by the Bay", "Jurong Bird Park", "Sentosa beaches"],
        "nightlife": ["Clarke Quay bars", "rooftop clubs", "night safari"]
    },
    "seoul": {
        "food": ["KBBQ night", "street food markets", "Hanbok cafe tour"],
        "culture": ["palace tour", "K-pop street", "traditional tea houses"],
        "nature": ["Namsan tower hike", "Bukhansan national park", "river biking"],
        "nightlife": ["Hongdae clubs", "karaoke bars", "late-night cafes"]
    },
    "sanfrancisco": {
        "food": ["sourdough tour", "mission burrito crawl", "seafood pier dining"],
        "culture": ["Golden Gate walk", "art district murals", "tech HQ tour"],
        "nature": ["Muir Woods trip", "beach sunset", "bay cruise"],
        "nightlife": ["downtown clubs", "jazz bars", "rooftop lounges"]
    }
}

#Function to get destination by budget
def get_destination_by_budget(budget: float):
    """Return the most suitable destination for a given budget."""
    possible = [d for d, cost in destinations.items() if cost <= budget]
    if not possible:
        return None
    return max(possible, key=lambda d: destinations[d])

#Function to generate itinerary based on user preference
def generate_itinerary(city, preference, days):
    if city not in preferences or preference not in preferences[city]:
        # Default activities if city or preference not found
        activities = ["city exploration", "local dining experience", "popular landmarks visit"]
    else:
        activities = preferences[city][preference]

    itinerary = []
    for i in range(days):
        activity = random.choice(activities)
        itinerary.append(f"Day {i+1}: {activity.title()} in {city.title()}")

    return itinerary
