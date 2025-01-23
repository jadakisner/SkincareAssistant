from flask import Flask, render_template, request
from main import get_recommendations, get_ai_advice  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = None
    ai_advice_cleanser = None
    ai_advice_lotion = None
    selected_skin_type = "oily"  # Default 

    if request.method == "POST":
        selected_skin_type = request.form.get("skin_type")
        recommendations = get_recommendations(selected_skin_type)
        ai_advice_cleanser = get_ai_advice(selected_skin_type, "cleansers")
        ai_advice_lotion = get_ai_advice(selected_skin_type, "lotions")

    return render_template("index.html", 
                           selected_skin_type=selected_skin_type, 
                           recommendations=recommendations, 
                           ai_advice_cleanser=ai_advice_cleanser, 
                           ai_advice_lotion=ai_advice_lotion)

if __name__ == "__main__":
    app.run(debug=True)