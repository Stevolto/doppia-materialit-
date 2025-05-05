from flask import Flask, request
from flask_babel import Babel
from modules.phase1_upload import bp as phase1_bp
from modules.phase2_analysis import bp as phase2_bp
from modules.phase3_kpis import bp as phase3_bp
from modules.phase4_report import bp as phase4_bp

app = Flask(__name__)
app.config.from_object('config.Config')

babel = Babel(app)
@babel.localeselector
def get_locale():
    return request.args.get('lang') or app.config['BABEL_DEFAULT_LOCALE']

app.register_blueprint(phase1_bp, url_prefix='/phase1')
app.register_blueprint(phase2_bp, url_prefix='/phase2')
app.register_blueprint(phase3_bp, url_prefix='/phase3')
app.register_blueprint(phase4_bp, url_prefix='/phase4')

@app.route('/')
def home():
    return "<h1>Double Materiality App</h1><p>Usa /phase1, /phase2, /phase3, /phase4</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
