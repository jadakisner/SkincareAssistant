from database import initialize_db, add_product

# Initialize the database
initialize_db()

# List of products to add
products = [
    ("Origins Checks and Balances Frothy Face Wash", "cleanser", "oily", "It rinses away impurities and makeup, helps purify pores of oils that can lead to blemishes, and leaves dry and oily zones comfortably clean. Plus, its rich texture lathers up to amplify its Mint-infused formula that helps invigorate the senses."),
    ("Peach and Lily Ginger Melt Cleanser", "cleanser", "oily", "Gently melt away all traces of makeup, sunscreen, oil, and impurities with our oil cleanser—super-sized. Rejuvenating antioxidant-rich blend of ginger root extract, sunflower, and grapeseed seed oil, and pineapple extract visibly clarifies and balances, without clogging pores or leaving a greasy residue. Reveal refreshed, hydrated, clear skin—fast."),
    ("Paula’s Choice Softening Cream Cleanser", "cleanser", "dry", "This skin-softening cream cleanser gently removes makeup without stripping skin of essential moisture. Hydrating ingredients replenish skin to keep a dewy beautiful glow."),
    ("La Roche Posay Toleraine Hydrating Gentle Cleanser", "cleanser", "dry", "Toleriane Hydrating Gentle Cleanser is a daily face wash for normal to dry, sensitive skin. Formulated with La Roche-Posay prebiotic thermal spring water, niacinamide, and ceramide-3, this face wash gently cleanses skin of dirt, makeup, and impurities while maintaining skin's natural moisture barrier and pH."),
    ("Rephr Gentle Cleanser", "cleanser", "combination", "Our gentle cleanser is a light foaming gel ready for everyday use. Part of our v1 skincare line available for community testing and feedback. The gentle cleanser 1.0 has been formulated with a slight acidic formula (pH 4.5) to maintain the skin's oil and water balance while washing away excess oil, direct, and skin waste."),
    ("Beauty of Joseon Green Plum", "cleanser", "combination", "Green Plum Refreshing Cleanser is a slightly acidic cleanser that helps to cleanse the face without damaging the natural skin barrier."),
    ("Clinique Moisture Surge 100h", "lotion", "oily", "Dermatologist-recommended facial moisturizer with aloe bioferment and hyaluronic acid delivers instant hydration that soothes in 3 seconds. 100% instantly show a boost in hydration and glow. "),
    ("Benefit POREfessional Smooth Sip", "lotion", "oily", "This lightweight moisturizer nourishes dry and oily skin types and its non-comedogenic formula is made specially for pores. Skin feels soft and texture looks smoother and more even over time. Plus, the water-based gel-cream is absorbed in record time for instant hydration. It’s like a summer swim that never has to end."),
    ("Tula 24/7 Hydrating Day and Night Cream", "lotion", "dry", "The perfect do-it-all moisturizer that hydrates for 24-hours.Lightweight, non-greasy cream. Revives the appearance of dull & tired skin. Infused with probiotic extracts, apple, watermelon, squalane, collagen & peptides. Leaves skin looking more supple, plump & glowy"),
    ("Peach and Lily Rescue Party Barrier Comfort Cream", "lotion", "dry", "This sumptuous cream soothes and smooths with 0.8% colloidal oatmeal, lactobacillus ferment, and Korean botanicals, while 5 ceramides, good fats, squalane and jojoba oil replenish and moisturize. A proprietary Calcium Complex nourishes with calcium, vital for healthy barrier function. Stay calm—your Rescue Party is here."),
    ("Peach and Lily Matcha Pudding", "lotion", "combination", "Drench skin in antioxidant-rich matcha with this lightweight, deeply moisturizing cream. Spiked with niacinamide, cape lilac, and adenosine, this silky, soothing formula visibly brightens, firms, and hydrates while helping to protect skin from free radical damage and stressors. Also helps prevent visible signs of aging for healthy-looking skin.."),
    ("Tatcha Water Cream", "lotion", "combination", "The Water Cream is a lightweight, oil-free gel cream that bursts to deliver 3x hydration* while visibly refining clogged pores & smoothing texture with a BHA alternative."),
    ("Good Molecules Lightweight Daily Moisturizer", "lotion", "normal", "The Good Molecules Lightweight Daily Moisturizer smoothes, hydrates, and preps your skin for makeup. The bestselling moisturizer was recently reformulated with avocado oil and even more hyaluronic acid to nourish and hydrate the skin while maintaining a lightweight texture.")
]

# Insert products while avoiding duplicates
for product in products:
    try:
        add_product(*product)
    except Exception as e:
        print(f"Skipping duplicate or invalid entry: {product[0]} - {e}")

print("Database setup completed. Products added successfully!")
