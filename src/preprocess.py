import pandas as pd

def preprocess_input(form, columns):
    
    features = {col: 0 for col in columns}

    #features["rating_clean"] = float(form["rating_clean"])
    features["price_winsor"] = float(form["price_winsor"])

    # One-hot encoding
    website = "website_" + form["website"]
    category = "category_" + form["category"]
    subcategory = "subcategory_" + form["subcategory"]
    country = "country_" + form["country"]

    if website in features: features[website] = 1
    if category in features: features[category] = 1
    if subcategory in features: features[subcategory] = 1
    if country in features: features[country] = 1

    return pd.DataFrame([features])