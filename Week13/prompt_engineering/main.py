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

        IMPORTANT FORMATTING INSTRUCTIONS:
        - Use **bold text** for important information like destinations, costs, and key activities
        - Use *italic text* for emphasis
        - Use # for main headings, ## for section headings, ### for subheadings
        - Use bullet points (*) for lists
        - Structure your response with clear sections and headings
        - Include budget information in **bold** for easy identification
        - Use line breaks to separate different activities and sections

        ESSENTIAL INFORMATION TO GATHER:
        - Destination (city/country)
        - Duration (number of days)
        - Travel dates or season
        - Budget range
        - Travel style (budget, mid-range, luxury)
        - Interests (culture, nature, food, adventure, history, etc.)
        - Group size and composition
        - Special requirements (accessibility, dietary restrictions, etc.)

        FOR ITINERARY REQUESTS, ALWAYS INCLUDE:
        1. Day-by-day breakdown with clear headings
        2. Specific locations with addresses
        3. Time estimates for each activity
        4. Transportation options between locations
        5. Budget estimates in **bold**
        6. Local tips and recommendations
        7. Alternative options for bad weather
        8. **Important**: Include practical travel tips (visa requirements, currency, language, weather, safety)

        RESPONSE GUIDELINES:
        - Be specific with addresses and exact locations
        - Include realistic time estimates (consider travel time between locations)
        - Suggest both free and paid activities
        - Mention local customs and cultural etiquette
        - Provide budget breakdowns per day
        - Include food recommendations (local specialties and budget options)
        - Suggest accommodation types suitable for the budget
        - No more than 1 activity on the first and last day of the itinerary
        - No more than 2 activities per day

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