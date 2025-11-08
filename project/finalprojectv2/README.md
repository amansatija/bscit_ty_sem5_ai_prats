# Sentiment Analysis Chatbot

A full-stack web application that analyzes the sentiment of text input using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool. The application features user authentication, real-time sentiment analysis, and chat history storage.

## Features

- 🔐 **User Authentication**: Secure registration and login with JWT tokens
- 💬 **Real-time Sentiment Analysis**: Analyze text sentiment instantly using VADER
- 📊 **Detailed Sentiment Scores**: View positive, negative, neutral, and compound scores
- 🔍 **Enhanced Analysis**: NEW! Get insights and confidence scores with detailed endpoint
- 🧪 **Test Samples**: NEW! Test VADER's capabilities with predefined examples
- 📝 **Chat History**: Store and view previous sentiment analyses
- 🎨 **Modern UI**: Beautiful, responsive interface built with React
- 🗄️ **MongoDB Integration**: Persistent storage for users and chat data

## Tech Stack

### Backend
- **Flask**: Python web framework
- **MongoDB**: NoSQL database for data storage
- **NLTK VADER**: Sentiment analysis engine
- **JWT**: Secure authentication
- **Flask-CORS**: Cross-origin resource sharing
- **Bcrypt**: Password hashing

### Frontend
- **React**: UI library
- **React Router**: Client-side routing
- **Axios**: HTTP client
- **Lucide React**: Modern icon library
- **CSS3**: Custom styling with gradients and animations

## Prerequisites

- Python 3.8+
- Node.js 14+
- MongoDB (local or cloud instance)
- npm or yarn

## Installation

### 1. Clone the Repository

```bash
cd /path/to/finalprojectv2
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env file with your MongoDB URI and JWT secret
# MONGO_URI=mongodb://localhost:27017/sentiment_app
# JWT_SECRET_KEY=your-secret-key-here
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install dependencies
npm install
```

### 4. MongoDB Setup

Make sure MongoDB is running:

```bash
# If using local MongoDB
mongod

# Or use MongoDB Atlas (cloud) and update MONGO_URI in .env
```

## Running the Application

### Start Backend Server

```bash
# From backend directory with venv activated
python app.py
```

The backend will run on `http://localhost:5000`

### Start Frontend Development Server

```bash
# From frontend directory
npm start
```

The frontend will run on `http://localhost:3000`

## Usage

1. **Register**: Create a new account with username, email, and password
2. **Login**: Sign in with your credentials
3. **Analyze Sentiment**: Type any text in the input box and click send
4. **View Results**: See the sentiment label (Positive/Negative/Neutral) with detailed scores
5. **Check History**: Click the history icon to view past analyses
6. **Logout**: Click the logout button when done

## API Endpoints

### Authentication
- `POST /api/register` - Register new user
- `POST /api/login` - Login user
- `GET /api/user` - Get current user info (requires JWT)

### Sentiment Analysis
- `POST /api/analyze` - Analyze text sentiment (requires JWT)
- `POST /api/analyze-detailed` - **NEW!** Enhanced analysis with insights (requires JWT)
- `GET /api/test-samples` - **NEW!** Test VADER with sample reviews (no auth required)
- `GET /api/history` - Get user's chat history (requires JWT)
- `DELETE /api/history/<chat_id>` - Delete a chat entry (requires JWT)

### Health Check
- `GET /api/health` - Check server status

> 📖 **See [SENTIMENT_IMPROVEMENTS.md](./SENTIMENT_IMPROVEMENTS.md) for detailed documentation on new features and enhancements.**

## Sentiment Analysis

The application uses NLTK's VADER sentiment analyzer which provides:

- **Compound Score**: Overall sentiment (-1 to +1)
  - ≥ 0.05: Positive 😊
  - ≤ -0.05: Negative 😡
  - Between: Neutral 😐
- **Positive Score**: Proportion of positive sentiment
- **Negative Score**: Proportion of negative sentiment
- **Neutral Score**: Proportion of neutral sentiment

## Project Structure

```
finalprojectv2/
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Environment variables template
│   └── .gitignore
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   │   ├── Chat.js
│   │   │   ├── Auth.css
│   │   │   └── Chat.css
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   └── .gitignore
└── README.md
```

## Security Features

- Password hashing with Bcrypt
- JWT token-based authentication
- Protected API routes
- CORS configuration
- Environment variable management

## Future Enhancements

- [ ] Export chat history to CSV/PDF
- [ ] Sentiment trend visualization
- [ ] Multi-language support
- [ ] Batch text analysis
- [ ] User profile management
- [ ] Dark mode theme
- [ ] Real-time collaboration

## Troubleshooting

### MongoDB Connection Issues
- Ensure MongoDB is running
- Check MONGO_URI in .env file
- Verify network connectivity for cloud MongoDB

### NLTK Data Issues
- The app automatically downloads VADER lexicon on first run
- If issues persist, manually download: `python -c "import nltk; nltk.download('vader_lexicon')"`

### Port Conflicts
- Backend default: 5000 (change in app.py)
- Frontend default: 3000 (change in package.json)

## License

This project is created for educational purposes.

## Contributors

- Your Name

## Acknowledgments

- NLTK VADER for sentiment analysis
- Flask and React communities
- MongoDB documentation
