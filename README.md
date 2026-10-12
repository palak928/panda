# 🐼 Panda Hub Mobile Detailing

**Professional Detailing. We Come to You.**

A premium, modern mobile car detailing website built with Python Flask, featuring an AI assistant chatbot, interactive service selection, and a complete booking system.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12+-green.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-red.svg)

---

## 🌟 Features

### 🎨 Premium Design
- **Dark Automotive Theme**: Professional dark charcoal (#06080B) background with cyan (#00E5FF) accents
- **Responsive Design**: Fully responsive layout optimized for mobile and desktop
- **Smooth Animations**: Hover effects, transitions, and micro-interactions
- **Modern UI**: Glass/blur effects, rounded cards, and clean typography

### 🤖 AI Assistant Chatbot
- **24/7 Customer Support**: Floating AI chatbot for instant assistance
- **Smart Responses**: Pre-built responses for common questions about pricing, booking, services, and more
- **Quick Suggestions**: One-tap question chips for fast navigation
- **Action Cards**: Interactive buttons to book services or navigate pages directly from chat

### 📱 Complete Website Pages
- **Homepage**: Hero section, interactive before/after slider, "What does your car need?" diagnostic, service packages overview
- **Services Page**: Vehicle type selector with dynamic pricing, three service tiers, add-on services
- **Booking Page**: Complete booking form with validation, consent checkboxes, and confirmation
- **About Page**: Company story, values, and future vision
- **FAQ Page**: Accordion-style frequently asked questions
- **Contact Page**: Contact form and business information
- **Cart Page**: Shopping cart with item management and pricing

### 🛠️ Interactive Features
- **Before/After Slider**: Drag-to-compare image slider showing transformation results
- **Vehicle Type Selector**: Dynamic pricing based on vehicle size (Sedan, SUV, Truck, Van, Luxury)
- **Diagnostic Tool**: Interactive "What does your car need?" section with service recommendations
- **FAQ Accordion**: Expandable/collapsible question-answer pairs
- **Cart Management**: Add/remove items, view totals, proceed to booking

### 🧭 Navigation
- **Back to Home Button**: Prominent navigation button on every page
- **Sticky Navigation**: Fixed header with logo and menu
- **Logo Navigation**: Click logo to return to homepage
- **Mobile Menu**: Responsive navigation for mobile devices

---

## 🚀 Technology Stack

### Backend
- **Python 3.12+**: Core programming language
- **Flask 3.0.0**: Web framework
- **Flask-CORS 4.0.0**: Cross-origin resource sharing

### Frontend
- **HTML5**: Structure and semantics
- **CSS3**: Styling with modern features (Flexbox, Grid, animations)
- **JavaScript (Vanilla)**: Interactive functionality and API calls
- **Responsive Design**: Mobile-first approach

### Development Tools
- **Git**: Version control
- **VS Code/Windsurf**: IDE support

---

## 📦 Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Git (for version control)

### Step 1: Clone the Repository
```bash
git clone https://github.com/palak928/panda.git
cd panda
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will start running on: **http://127.0.0.1:5000**

---

## 📁 Project Structure

```
panda/
├── app.py                 # Flask application with routes and API endpoints
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation and AI assistant
│   ├── index.html        # Homepage
│   ├── services.html     # Services page
│   ├── booking.html      # Booking form
│   ├── about.html        # About page
│   ├── faq.html          # FAQ page
│   ├── contact.html      # Contact page
│   └── cart.html         # Shopping cart
└── .devin/               # Devin configuration (optional)
```

---

## 🔌 API Endpoints

### Web Routes
- `GET /` - Homepage
- `GET /services` - Services page
- `GET /booking` - Booking page
- `GET /about` - About page
- `GET /faq` - FAQ page
- `GET /contact` - Contact page
- `GET /cart` - Cart page

### API Routes
- `POST /api/ai-chat` - AI assistant chatbot endpoint
  - Request: `{ "message": "user question" }`
  - Response: `{ "response": "AI answer", "suggestions": ["action1", "action2"] }`

- `POST /api/booking` - Booking submission endpoint
  - Request: Booking form data (name, email, phone, vehicle, service, etc.)
  - Response: `{ "success": true, "booking_id": "PH-2026-000001", "message": "..." }`

---

## 🎯 Service Packages

### Essential - The Refresh ($129+)
- Exterior wash
- Interior vacuum
- Dashboard cleaning
- Window cleaning
- Tire treatment
- Duration: 1.5-2 hours

### Complete - The Transformation ($229+) ⭐ Most Popular
- Everything in Essential
- Deep interior cleaning
- Seat cleaning
- Carpet treatment
- Detailed exterior cleaning
- Additional finishing services
- Duration: 3-4 hours

### Premium - The Showroom ($349+)
- Everything in Complete
- Paint correction
- Ceramic coating
- Engine bay detailing
- Headlight restoration
- Premium finishing
- Duration: 5-6 hours

### Add-On Services
- Pet Hair Removal (+$49)
- Stain Treatment (+$39)
- Odor Treatment (+$59)
- Headlight Restoration (+$79)

---

## 🎨 Design Features

### Color Palette
- **Primary Background**: #06080B (Deep charcoal)
- **Secondary Background**: #0E1015 (Dark gray)
- **Accent Color**: #00E5FF (Cyan)
- **Text**: #FFFFFF (White)
- **Muted Text**: rgba(255, 255, 255, 0.7)

### Typography
- **Headings**: Segoe UI, bold, large sizes
- **Body**: Segoe UI, regular, readable sizes
- **Accents**: Clean sans-serif fonts

### Interactive Elements
- **Buttons**: Gradient backgrounds with hover lift effects
- **Cards**: Subtle borders with hover transforms
- **Inputs**: Dark backgrounds with focus highlights
- **Animations**: Smooth transitions and micro-interactions

---

## 📱 Pages Overview

### Homepage
- Hero section with "YOUR CAR. OUR CANVAS." headline
- Interactive before/after transformation slider
- "What does your car need?" diagnostic tool
- Service packages preview
- "How it works" 4-step process
- Footer with navigation links

### Services Page
- Vehicle type selector (Sedan, SUV, Truck, Van, Luxury)
- Dynamic pricing based on vehicle size
- Three service package cards with details
- Add-on services grid
- "Book Now" buttons for each package

### Booking Page
- Customer information form (name, email, phone)
- Vehicle information (type, make/model)
- Service selection (package, add-ons)
- Appointment details (date, time, location)
- Additional notes field
- Consent checkboxes (notifications, marketing)
- Form validation
- Success confirmation with booking ID

### About Page
- Company story and mission
- Why choose Panda Hub section
- Four value pillars
- Future expansion plans
- Mobile unit specifications

### FAQ Page
- 10+ frequently asked questions
- Accordion-style expand/collapse
- Topics: mobile service, timing, requirements, pet hair, frequency, etc.

### Contact Page
- Contact form (name, email, phone, service, message)
- Service area information
- Business contact details

### Cart Page
- Selected services display
- Item removal functionality
- Subtotal, tax, and total calculation
- "Continue to Booking" button
- "Continue Shopping" link

---

## 🔧 Configuration

### Environment Variables (Optional)
The application can be configured with environment variables for production deployment:
- `FLASK_ENV`: Set to `production` for production mode
- `FLASK_DEBUG`: Set to `False` for production
- Custom email/SMS API keys (for real notification integration)

### Customization
- **Colors**: Modify CSS variables in `base.html`
- **Pricing**: Update prices in service pages
- **AI Responses**: Modify response logic in `app.py`
- **Content**: Edit HTML templates directly

---

## 🚢 Deployment

### PythonAnywhere
1. Create a PythonAnywhere account
2. Create a new web app
3. Upload files via Git or drag-and-drop
4. Install requirements in virtual environment
5. Configure WSGI file
6. Set up static files

### Heroku
1. Install Heroku CLI
2. Create `Procfile`: `web: python app.py`
3. Create `runtime.txt`: `python-3.12.10`
4. Push to Heroku:
   ```bash
   heroku create
   git push heroku main
   ```

### Vercel/Railway/Render
- Similar deployment processes with platform-specific configurations

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Future Enhancements

- [ ] Real email/SMS notification integration
- [ ] Database integration for booking storage
- [ ] User authentication and account system
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Admin dashboard for booking management
- [ ] Real-time availability calendar
- [ ] Customer reviews and ratings
- [ ] Before/after image gallery
- [ ] Blog section for car care tips
- [ ] Multi-language support
- [ ] Mobile app development

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Palak Garg**
- GitHub: [@palak928](https://github.com/palak928)
- Project: Panda Hub Mobile Detailing

---

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Inspired by modern automotive service platforms
- Developed as an academic e-commerce and digital marketing project

---

## 📞 Support

For questions or support:
- Email: info@pandahub.ca
- Phone: (416) 555-PANDA
- GitHub Issues: [Create an issue](https://github.com/palak928/panda/issues)

---

## 🌐 Live Demo

The website is currently running locally at: **http://127.0.0.1:5000**

To run the application:
```bash
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000`

---

**Panda Hub Mobile Detailing - Professional Detailing. We Come to You.** 🐼✨
