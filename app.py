from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/api/ai-chat', methods=['POST'])
def ai_chat():
    """AI Assistant Chatbot Endpoint"""
    data = request.json
    user_message = data.get('message', '').lower()
    
    # Simple AI response logic (can be enhanced with real AI)
    responses = {
        'price': 'Our services start at $129 for Essential, $229 for Complete, and $349 for Premium. Prices vary by vehicle size.',
        'booking': 'You can book by clicking the "Book Now" button on any service page or using the cart.',
        'pet hair': 'We offer specialized pet hair removal using electrostatic tools and hot-water extraction. It\'s included in our Complete and Premium packages.',
        'location': 'We come to your location! Our mobile detailing units serve the GTA, Vancouver, Calgary, and Montreal areas.',
        'time': 'Essential takes 1.5-2 hours, Complete takes 3-4 hours, and Premium takes 5-6 hours.',
        'appointment': 'Same-day appointments are often available based on our schedule. Book online to check availability.',
        'cancel': 'You can cancel by logging into your account or contacting us at least 24 hours before your appointment.',
        'packages': 'We offer three packages: Essential (basic refresh), Complete (deep clean - most popular), and Premium (showroom finish).',
        'payment': 'We accept credit cards, debit, and e-transfer. Payment is collected after service completion.',
        'default': 'I\'m here to help! You can ask me about our services, pricing, booking, or any car care questions. What would you like to know?'
    }
    
    # Find matching response
    response = responses['default']
    for keyword, answer in responses.items():
        if keyword != 'default' and keyword in user_message:
            response = answer
            break
    
    return jsonify({
        'response': response,
        'suggestions': [
            'Book Complete Detail ($229)',
            'View Service Packages',
            'Check Availability'
        ]
    })

@app.route('/api/booking', methods=['POST'])
def create_booking():
    """Handle booking submissions"""
    data = request.json
    
    # Generate booking ID
    booking_id = f"PH-2026-{str(len(data.get('name', '')) + 1000).zfill(6)}"
    
    # In a real app, this would save to a database
    return jsonify({
        'success': True,
        'booking_id': booking_id,
        'message': 'Booking confirmed! Check your email for details.'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
