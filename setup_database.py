from database import initialize_db, add_product

initialize_db()

products = [
    ("Origins Checks and Balances Frothy Face Wash", "cleanser", "oily", "A frothy face wash for oily skin."),
    ("Peach and Lily Ginger Melt Cleanser", "cleanser", "oily", "A gentle cleanser for oily skin."),
    ("Paula’s Choice Softening Cream Cleanser", "cleanser", "dry", "A hydrating cream cleanser for dry skin."),
    ("La Roche Posay Toleraine Hydrating Gentle Cleanser", "cleanser", "dry", "A gentle hydrating cleanser for dry skin."),
    ("Rephr Gentle Cleanser", "cleanser", "combination", "A gentle cleanser for combination skin."),
    ("Beauty of Joseon Green Plum", "cleanser", "combination", "A refreshing cleanser for combination skin."),
    ("Clinique Moisture Surge 100h", "lotion", "oily", "A lightweight moisturizer for oily skin."),
    ("Benefit Smooth Sip", "lotion", "oily", "A mattifying lotion for oily skin."),
    ("Tula 24/7 Moisturizer", "lotion", "dry", "A deeply hydrating moisturizer for dry skin."),
    ("Peach and Lily Rescue Party Barrier Comfort Cream", "lotion", "dry", "A barrier-restoring cream for dry skin."),
    ("Peach and Lily Matcha Pudding", "lotion", "combination", "A lightweight moisturizer for combination skin."),
    ("Tatcha Water Cream", "lotion", "combination", "A hydrating water cream for combination skin."),
    ("Good Molecules Lightweight Daily Moisturizer", "lotion", "normal", "A balanced moisturizer for normal skin.")
]

for product in products:
    add_product(*product)
