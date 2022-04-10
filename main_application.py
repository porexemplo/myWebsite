from flask import Flask, render_template
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__name__)
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=1)
def home():
    return render_template('home.html')


if __name__ == '__main__': app.run(debug=True)