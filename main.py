import openai
from database import get_products_by_skin_type

openai.api_key = ""  

def get_skin_type_or_concern():
    """
    Get the user's skin type selection from the form.
    """
    while True:
        print("\nWhat is your skin type or specific concern?:")
        print("1. Oily")
        print("2. Dry")
        print("3. Combination")
        print("4. Normal")
        
        skin_type = input("Enter the number corresponding to your skin type/concern: ").strip()
        if skin_type in ["1", "2", "3", "4"]:
            return ["oily", "dry", "combination", "normal"][int(skin_type) - 1]
        else:
            print("Invalid input, please enter a number between 1 and 4.")

def get_ai_advice(skin_type, product_type):
    """
    Fetch AI-generated skincare advice from OpenAI API based on skin type and product category.
    """
    prompt = (
        f"Provide detailed skincare advice for someone with {skin_type} skin, "
        f"focusing on effective {product_type} with specific ingredients and application tips."
        f"Break the advice into short, distinct points with numbered or bullet formatting."
    )
    
    try:
        response = openai.chat.completions.create( 
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content

    except openai.OpenAIError as e: 
        print(f"Error generating AI advice: {e}")
        return "We encountered an issue generating AI advice. Please try again later."

def get_recommendations(skin_type):
    """
    Fetch product recommendations from the database for the given skin type.
    Categorizes them into cleansers and lotions.
    """
    recommendations = get_products_by_skin_type(skin_type)

    cleansers = [product for product in recommendations if product[1] == "cleanser"]
    lotions = [product for product in recommendations if product[1] == "lotion"]

    return {"cleansers": cleansers, "lotions": lotions}

def main():
    """
    Run the Skincare Assistant CLI version.
    """
    print("Welcome to your personalized Skincare Assistant!")

    # user's skin type
    skin_type = get_skin_type_or_concern()

    # Fetch recommendations from the database
    recommendations = get_recommendations(skin_type)

    # Display Cleansers
    if recommendations["cleansers"]:
        print("\nRecommended Cleansers:")
        for name, type, description in recommendations["cleansers"]:
            print(f"- {name} ({type}): {description}")
        ai_advice_cleanser = get_ai_advice(skin_type, "cleansers")
        print("\nAI Advice for Cleansers:")
        print(ai_advice_cleanser)

    # Display Lotions
    if recommendations["lotions"]:
        print("\nRecommended Lotions:")
        for name, type, description in recommendations["lotions"]:
            print(f"- {name} ({type}): {description}")
        ai_advice_lotion = get_ai_advice(skin_type, "lotions")
        print("\nAI Advice for Lotions:")
        print(ai_advice_lotion)

if __name__ == "__main__":
    main()
