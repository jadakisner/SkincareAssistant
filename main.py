import openai
from database import initialize_db, add_product, get_products_by_skin_type

# Set your OpenAI API key
openai.api_key = ""

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

def get_ai_advice(skin_type, product_type):
    # Generate personalized skincare advice using OpenAI's gpt-3.5-turbo model
    prompt = f"Provide skincare advice for someone with {skin_type} skin, focusing on {product_type}."
    
    # Updated API call using the new OpenAI library
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or another available model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    
    return response['choices'][0]['message']['content']

def main():
    print("Welcome to your personalized Skincare Assistant!")

    # Initialize the database
    initialize_db()

    # Example: Adding some products to the database
    add_product("Origins Checks and Balances Frothy Face Wash", "cleanser", "oily", "A frothy face wash for oily skin.")
    add_product("Peach and Lily Ginger Melt Cleanser", "cleanser", "oily", "A gentle cleanser for oily skin.")
    add_product("Paula’s Choice Softening Cream Cleanser", "cleanser", "dry", "A hydrating cream cleanser for dry skin.")
    add_product("La Roche Posay Toleraine Hydrating Gentle Cleanser", "cleanser", "dry", "A gentle hydrating cleanser for dry skin.")
    add_product("Rephr Gentle Cleanser", "cleanser", "combination", "A gentle cleanser for combination skin.")
    add_product("Beauty of Joseon Green Plum", "cleanser", "combination", "A refreshing cleanser for combination skin.")
    add_product("Clinique Moisture Surge 100h", "lotion", "oily", "A lightweight moisturizer for oily skin.")
    add_product("Benefit Smooth Sip", "lotion", "oily", "A mattifying lotion for oily skin.")
    add_product("Tula 24/7 Moisturizer", "lotion", "dry", "A deeply hydrating moisturizer for dry skin.")
    add_product("Peach and Lily Rescue Party Barrier Comfort Cream", "lotion", "dry", "A barrier-restoring cream for dry skin.")
    add_product("Peach and Lily Matcha Pudding", "lotion", "combination", "A lightweight moisturizer for combination skin.")
    add_product("Tatcha Water Cream", "lotion", "combination", "A hydrating water cream for combination skin.")
    add_product("Good Molecules Lightweight Daily Moisturizer", "lotion", "normal", "A balanced moisturizer for normal skin.")

    # Get user skin type or concerns
    skin_type = get_skin_type_or_concern()

    # Fetch and display recommendations from the database
    recommendations = get_products_by_skin_type(skin_type)

    # Categorize the recommendations into cleansers and lotions
    cleansers = [product for product in recommendations if product[1] == "cleanser"]
    lotions = [product for product in recommendations if product[1] == "lotion"]

    # Display cleansers
    if cleansers:
        print("\nRecommended Cleansers:")
        for product in cleansers:
            name, type, description = product
            print(f"- {name} ({type}): {description}")
        
        # Get AI advice for cleansers
        ai_advice_cleanser = get_ai_advice(skin_type, "cleansers")
        print("\nAI Advice for Cleansers:")
        print(ai_advice_cleanser)
    
    # Display lotions
    if lotions:
        print("\nRecommended Lotions:")
        for product in lotions:
            name, type, description = product
            print(f"- {name} ({type}): {description}")
        
        # Get AI advice for lotions
        ai_advice_lotion = get_ai_advice(skin_type, "lotions")
        print("\nAI Advice for Lotions:")
        print(ai_advice_lotion)

if __name__ == "__main__":
    main()
