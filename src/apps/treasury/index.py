import dash
from dash_extensions.enrich import html
from flask_caching import Cache

from src.apps.treasury.app import app
from src.apps.treasury.util.constants import CACHE_TIMEOUT

CONTENT_STYLE = {
    "position": "relative",
    "margin-right": "0rem",
    "margin-left": "0rem",
    "background-color": "#FFF",
    "height": "100vh"
}
FOOTER_STYLE = {
    "position": "relative",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": "6rem",
    "padding": "1rem 1rem",
    "background-color": "#FFF",
}

cache = Cache(
    app.server,
    config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': '/tmp/cache-directory',
        'CACHE_DEFAULT_TIMEOUT': CACHE_TIMEOUT
    }
)


@cache.memoize()
def get_layout():
    return html.Div([
        dash.page_container
    ])


app.layout = get_layout

# For Gunicorn to reference
server = app.server


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
