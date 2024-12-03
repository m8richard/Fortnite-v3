# Gentle Mates Fortnite Stats

A web application for visualizing Fortnite player statistics from tournaments.

## Features

- Player selection from dropdown
- Tournament filtering based on selected player
- Round selection for specific tournaments
- Detailed player statistics display
- Dark/Light theme toggle
- Responsive design

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:8050`

## Project Structure

```
static/
├── css/
│   └── style.css
└── js/
    └── script.js
templates/
└── index.html
images/
└── logo.png
README.md
app.py
requirements.txt
vercel.json
```

## Development

The application is built using:
- Dash framework for Python
- Plotly for data visualization
- Bootstrap for styling
- Custom CSS for theme switching

## Deployment

The application is configured for deployment on Vercel using the provided `vercel.json` configuration file.