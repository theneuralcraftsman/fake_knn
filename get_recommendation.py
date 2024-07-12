import numpy as np
from clothing_data import clothing_items

def calculate_distance(item1, item2):
    return np.abs(item1 - item2)

def get_recommendations(category, subcategory, item):
    recommendations = []
    item_encoding = clothing_items[category][subcategory][item]
    
    for cat in clothing_items:
        for subcat in clothing_items[cat]:
            for cloth, encoding in clothing_items[cat][subcat].items():
                if encoding != item_encoding:
                    distance = calculate_distance(item_encoding, encoding)
                    recommendations.append((cloth, distance))
                    
    recommendations.sort(key=lambda x: x[1])
    return [rec[0] for rec in recommendations[:5]]  # Return top 5 recommendations
