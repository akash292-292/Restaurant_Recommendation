class RestaurantRecommendationSystem:
    def __init__(self):
        # Define a data structure to store information about restaurants and their cuisines
        self.restaurants = {
            'Italian Trattoria': {'cuisine': 'Italian', 'rating': 4.5, 'proximity': 3},
            'Spice Paradise': {'cuisine': 'Indian', 'rating': 4.2, 'proximity': 2},
            'Sushi Delight': {'cuisine': 'Japanese', 'rating': 4.0, 'proximity': 5},
            'Taco Haven': {'cuisine': 'Mexican', 'rating': 4.8, 'proximity': 1},
            'Burger Spot': {'cuisine': 'American', 'rating': 4.1, 'proximity': 4},
            'Pizza Palace': {'cuisine': 'Italian', 'rating': 4.3, 'proximity': 2},
            'Noodle House': {'cuisine': 'Chinese', 'rating': 3.9, 'proximity': 3},
            'Fusion Grill': {'cuisine': 'Fusion', 'rating': 4.4, 'proximity': 4},
            'Sizzling BBQ': {'cuisine': 'Barbecue', 'rating': 4.7, 'proximity': 2},
            'Seafood Delight': {'cuisine': 'Seafood', 'rating': 4.6, 'proximity': 3},
            'Veggie Haven': {'cuisine': 'Vegetarian', 'rating': 4.2, 'proximity': 1},
            'Mediterranean Delight': {'cuisine': 'Mediterranean', 'rating': 4.0, 'proximity': 5},
            'Cafe de Paris': {'cuisine': 'French', 'rating': 4.5, 'proximity': 2},
            'Tandoori Express': {'cuisine': 'Indian', 'rating': 4.2, 'proximity': 3},
            'Steakhouse Supreme': {'cuisine': 'Steakhouse', 'rating': 4.4, 'proximity': 4},
            'Sizzling Wok': {'cuisine': 'Asian', 'rating': 4.3, 'proximity': 2},
            'Cheesy Bites': {'cuisine': 'Pizza', 'rating': 4.2, 'proximity': 3},
            'Grilled Greens': {'cuisine': 'Vegetarian', 'rating': 4.6, 'proximity': 1},
            'Hot Pot Haven': {'cuisine': 'Chinese', 'rating': 4.0, 'proximity': 5},
            'Tasty Tacos': {'cuisine': 'Mexican', 'rating': 4.5, 'proximity': 2},
            'Sunny Sushi': {'cuisine': 'Japanese', 'rating': 4.1, 'proximity': 4},
            'Smokehouse BBQ': {'cuisine': 'Barbecue', 'rating': 4.8, 'proximity': 1},
            'Pasta Paradise': {'cuisine': 'Italian', 'rating': 4.2, 'proximity': 3},
            'Gourmet Grill': {'cuisine': 'Fusion', 'rating': 4.4, 'proximity': 2}
        }

        # Set to store all cuisines
        self.all_cuisines = set(restaurant_info['cuisine'].lower() for restaurant_info in self.restaurants.values())

    def recommend_restaurants(self, food_type):
        food_type = food_type.lower()

        # Checking if the user's input is a valid cuisine
        if food_type not in self.all_cuisines:
            raise ValueError(f"Sorry, we do not have recommendations for the cuisine: {food_type}")

        # Filtering restaurants based on the given food type
        matching_restaurants = [restaurant for restaurant, info in self.restaurants.items() if
                                info['cuisine'].lower() == food_type]

        # Sorting restaurants based on a combination of rating and proximity
        sorted_restaurants = sorted(
            matching_restaurants,
            key=lambda x: (self.restaurants[x]['rating'], -self.restaurants[x]['proximity']),
            reverse=True
        )

        return sorted_restaurants


def main():
    try:
        # User input for the type of food
        user_input = input("Enter the type of food you're craving: ").strip()
        if len(user_input) == 0:
            print("No Input Entered")
            return 0

        # Initializing the recommendation system
        recommendation_system = RestaurantRecommendationSystem()
        # Getting restaurant recommendations
        recommendations = recommendation_system.recommend_restaurants(user_input)

        # Displaying recommendations
        print("\nRestaurant Recommendations:")
        for i, restaurant in enumerate(recommendations, start=1):
            print(
                f"{i}. {restaurant} - Cuisine: {recommendation_system.restaurants[restaurant]['cuisine']}, "
                f"Rating: {recommendation_system.restaurants[restaurant]['rating']}, "
                f"Proximity: {recommendation_system.restaurants[restaurant]['proximity']} km")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
