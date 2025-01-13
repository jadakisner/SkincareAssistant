def get_skin_type_or_concern():
    print("\nWhat is your skin type or specific concern?:")
    print("1. Oily")
    print("2. Dry")
    print("3. Combination")
    print("4. Normal")
    
    skin_type = input("Enter the number corresponding to your skin type/concern: ").strip()
    
    if skin_type == "1":
        return "oily"
    elif skin_type == "2":
        return "dry"
    elif skin_type == "3":
        return "combination"
    elif skin_type == "4":
        return "normal"
    else:
        print("Invalid input, please enter a number between 1 and 4.")
        return get_skin_type_or_concern()

def generate_recommendations(skin_type):
    recommendations = []

    # Face wash recommendations based on skin type
    if skin_type == "oily":
        recommendations.append("\nWe recommend 2 cleansers for oily skin: \n1. Origins Checks and Balances Frothy Face Wash\n2. Peach and Lily Ginger Melt Cleanser")
    elif skin_type == "dry":
        recommendations.append("\nWe recommend 2 hydrating cleansers: \n1. Paula’s Choice Softening Cream Cleanser\n2. La Roche Posay Toleraine Hydrating Gentle Cleanser")
    elif skin_type == "combination":
        recommendations.append("\nWe recommend 2 cleansers for combination skin: \n1. Rephr Gentle Cleanser\n2. Beauty of Joseon Green Plum")
    elif skin_type == "normal":
        recommendations.append("\nWe recommend 3 cleansers for normal skin: \n1. Green Plum by Beauty of Joseon\n2. Rephr Cleanser\n3. Dermalogica Daily Milkfoliant")

    # Face lotion recommendations based on skin type
    if skin_type == "oily":
        recommendations.append("\nWe recommend 2 lotions for oily skin: \n1. Clinique Moisture Surge 100h\n2. Benefit Smooth Sip")
    elif skin_type == "dry":
        recommendations.append("\nWe have 2 lotion recommendations for dry skin: \n1. Tula 24/7 Moisturizer\n2. Peach and Lily Rescue Party Barrier Comfort Cream")
    elif skin_type == "combination":
        recommendations.append("\nWe recommend 2 lotions for combination skin: \n1. Peach and Lily Matcha Pudding\n2. Tatcha Water Cream")
    elif skin_type == "normal":
        recommendations.append("\nWe have 3 lotion recommendations for normal skin: \n1. Peach & Lily Matcha Pudding\n2. Clinique Moisture Surge 100h\n3. Good Molecules Lightweight Daily Moisturizer")

    return recommendations

def main():
    print("Welcome to your personalized Skincare Assistant!")

    # Get user skin type or concerns
    skin_type = get_skin_type_or_concern()

    # Generate and display recommendations
    recommendations = generate_recommendations(skin_type)

    print("\nYour personalized skincare recommendations:")
    for recommendation in recommendations:
        print(f"- {recommendation}")

if __name__ == "__main__":
    main()
