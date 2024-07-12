from flask import Flask, request, jsonify
from get_recommendation import get_recommendations
from clothing_data import clothing_items

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    category = request.args.get('category')
    subcategory = request.args.get('subcategory')
    item = request.args.get('item')
    
    if category not in clothing_items:
        return jsonify({'error': 'Invalid category'}), 400
    if subcategory not in clothing_items[category]:
        return jsonify({'error': 'Invalid subcategory'}), 400
    if item not in clothing_items[category][subcategory]:
        return jsonify({'error': 'Invalid item'}), 400
    
    recommendations = get_recommendations(category, subcategory, item)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
