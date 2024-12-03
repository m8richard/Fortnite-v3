import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

# Initialize the Dash app with Bootstrap for styling
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Placeholder data
PLAYERS = ["M8 PodaSai", "Player2", "Player3", "Player4"]
TOURNAMENTS = {
    "M8 PodaSai": ["FNCS Major 1", "FNCS Major 2", "DreamHack"],
    "Player2": ["FNCS Major 1", "Cash Cup"],
    "Player3": ["DreamHack", "Cash Cup"],
    "Player4": ["FNCS Major 1", "FNCS Major 2"],
}
ROUNDS = {
    "FNCS Major 1": ["Round 1", "Round 2", "Round 3"],
    "FNCS Major 2": ["Round 1", "Round 2", "Finals"],
    "DreamHack": ["Qualifiers", "Semi-Finals", "Finals"],
    "Cash Cup": ["Round 1", "Finals"],
}
STATS = {
    ("M8 PodaSai", "FNCS Major 1", "Round 1"): {
        "Eliminations": 15,
        "Assists": 5,
        "Damage dealt": 3500,
        "Damage taken": 2800,
        "Hits to Players": 85,
        "Damage to Players": 2900,
        "Headshots": 12,
        "Allies revived": 2,
        "Average placement": 4.5
    }
}

app.layout = html.Div([
    # Header
    html.Div([
        html.Div([
            html.Img(src='/assets/images/logo.png', className='logo'),
            html.H1("Gentle Mates Fortnite Stats", className='title'),
        ], className='header-left'),
        html.Button(
            "Toggle Theme",
            id='theme-toggle',
            className='theme-toggle-btn'
        ),
    ], className='header'),
    
    # Main content
    html.Div([
        # Dropdowns
        html.Div([
            dcc.Dropdown(
                id='player-dropdown',
                options=[{'label': player, 'value': player} for player in PLAYERS],
                placeholder="Select a player",
                className='dropdown'
            ),
            html.Div(id='tournament-dropdown-container'),
            html.Div(id='round-dropdown-container'),
        ], className='dropdowns-container'),
        
        # Stats display
        html.Div(id='stats-display', className='stats-container')
    ], className='main-content')
], id='main-container')

@app.callback(
    Output('tournament-dropdown-container', 'children'),
    [Input('player-dropdown', 'value')]
)
def update_tournament_dropdown(selected_player):
    if not selected_player:
        return []
    return dcc.Dropdown(
        id='tournament-dropdown',
        options=[{'label': t, 'value': t} for t in TOURNAMENTS.get(selected_player, [])],
        placeholder="Select a tournament",
        className='dropdown'
    )

@app.callback(
    Output('round-dropdown-container', 'children'),
    [Input('tournament-dropdown', 'value')]
)
def update_round_dropdown(selected_tournament):
    if not selected_tournament:
        return []
    return dcc.Dropdown(
        id='round-dropdown',
        options=[{'label': r, 'value': r} for r in ROUNDS.get(selected_tournament, [])],
        placeholder="Select a round",
        className='dropdown'
    )

@app.callback(
    Output('stats-display', 'children'),
    [Input('player-dropdown', 'value'),
     Input('tournament-dropdown', 'value'),
     Input('round-dropdown', 'value')]
)
def update_stats(player, tournament, round_):
    if not all([player, tournament, round_]):
        return []
    
    stats = STATS.get((player, tournament, round_), {})
    if not stats:
        return html.Div("No stats available for this selection", className='no-stats')
    
    return [
        html.Div([
            html.H3(f"{stat}: {value}", className='stat-item')
        ]) for stat, value in stats.items()
    ]

@app.callback(
    Output('main-container', 'className'),
    [Input('theme-toggle', 'n_clicks')],
    [State('main-container', 'className')]
)
def toggle_theme(n_clicks, current_class):
    if n_clicks is None:
        return 'light-theme'
    return 'dark-theme' if current_class == 'light-theme' else 'light-theme'

if __name__ == '__main__':
    app.run_server(debug=True)