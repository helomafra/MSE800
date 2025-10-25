import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

print(f"API Key loaded: {GEMINI_API_KEY is not None}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        travel_prompt = f"""
        You are a professional AI Travel Planner and Itinerary Expert. Your role is to provide personalized travel recommendations and create detailed itineraries.

        When users ask about travel planning, gather the following information if not provided:
        - Destination (city/country)
        - Duration (number of days)
        - Travel dates or season
        - Budget range
        - Travel style (budget, mid-range, luxury)
        - Interests (culture, nature, food, adventure, history, etc.)
        - Group size and composition
        - Special requirements (accessibility, dietary restrictions, etc.)

        For itinerary requests, provide:
        1. Day-by-day breakdown
        2. Specific locations with addresses
        3. Time estimates for each activity
        4. Transportation options between locations
        5. Budget estimates
        6. Local tips and recommendations
        7. Alternative options for bad weather

        Always be helpful, detailed, and consider practical aspects of travel planning.

        User's message: {user_message}
        """
        
        request_body = {
            "contents": [{"role": "user", "parts": [{"text": travel_prompt}]}]
        }
        
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-001:generateContent?key={GEMINI_API_KEY}",
            headers={'Content-Type': 'application/json'},
            json=request_body
        )
        
        data = response.json()
        
        if response.status_code == 200 and 'candidates' in data:
            ai_response = data['candidates'][0]['content']['parts'][0]['text']
            return jsonify({'status': 'success', 'response': ai_response})
        else:
            error_msg = data.get('error', {}).get('message', 'Unknown error occurred')
            return jsonify({'status': 'error', 'error': f'API Error: {error_msg}'})
            
    except Exception as e:
        return jsonify({'status': 'error', 'error': f'Server error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)