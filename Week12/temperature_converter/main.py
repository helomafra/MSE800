from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        temperature = float(data['temperature'])
        from_unit = data['from_unit']
        to_unit = data['to_unit']
        
        # Convert to Celsius first, then to target unit
        if from_unit == 'celsius':
            celsius = temperature
        elif from_unit == 'fahrenheit':
            celsius = fahrenheit_to_celsius(temperature)
        elif from_unit == 'kelvin':
            celsius = kelvin_to_celsius(temperature)
        
        # Convert from Celsius to target unit
        if to_unit == 'celsius':
            result = celsius
        elif to_unit == 'fahrenheit':
            result = celsius_to_fahrenheit(celsius)
        elif to_unit == 'kelvin':
            result = celsius_to_kelvin(celsius)
        
        return jsonify({
            'success': True,
            'result': round(result, 2),
            'from_unit': from_unit,
            'to_unit': to_unit
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5102)
 