import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import base64
import os
import dash_auth
from flask_login import LoginManager
import base64
from flask import Flask, Response

# Create Flask server
server = Flask(__name__)

# Define health check endpoints
@server.route("/healthz")
def healthz():
    return Response("OK", status=200)

@server.route("/readyz")
def readyz():
    return Response("OK", status=200)

# Initialize the Dash app with the Flask server
app = Dash(__name__, server=server)

# Function to add authentication to the app
def create_auth_app(app):
    VALID_USERNAME_PASSWORD_PAIRS = {
        'Devotee4234': 'Ref0rmed-Ant@rctic-Endpoint0'
    }
    auth = dash_auth.BasicAuth(
        app,
        VALID_USERNAME_PASSWORD_PAIRS
    )
    return app

# Add authentication to the app
app = create_auth_app(app)

# Encode the logo
with open("ICASA_Logo.jpg", "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

def create_dash_app(question_mapping):
    # Set a secret key to resolve the session warning
    app.server.secret_key = '24-unm-basic-needs-dashboard' 
    
    # Initialize LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app.server)
    
    # List to store tab contents
    tabs = []
    
    # Define the layout of the app
    app.layout = html.Div([
        html.H1("UNM Basic Needs Survey- Comprehensive Analysis of Open-Ended Questions"),
        dcc.Tabs(tabs),
        html.Footer([
            html.Img(src=f'data:image/png;base64,{encoded_logo}', style={'height': '50px', 'float': 'left'}),
            html.P("© 2024 New Mexico Tech - Institute for Complex Additive Systems Analysis. All rights reserved.",
                style={'float': 'right', 'margin-right': '20px'})
        ], style={'position': 'fixed', 'bottom': '0', 'width': '100%', 'background-color': '#f1f1f1', 'padding': '10px'})
    ])
    
    return app

if __name__ == "__main__":
    # Define the mapping of questions to their corresponding column names
    question_mapping = {
        "How is food or housing insecurity affecting your work?": "OE1",
        "What could your college or university do to address food and housing insecurity? Please share a solution(s).": "OE2",
        "Is there anything else you would like to share?": "OE3",
        "Please select the reasons for not visiting the campus food pantry.": "Foodpantry_reasons",
        "What are your thoughts about food availability on your campus?": "Foodavail",
        "Please share why you feel unsafe?": "Unsafe_why",
        "Please explain why it is difficult to find housing either on-campus or off-campus?": "Housingdiff_why"
    }
    
    # Create and run the app
    app = create_dash_app(question_mapping)
    app.run_server(debug=True, host='0.0.0.0', port=8080)