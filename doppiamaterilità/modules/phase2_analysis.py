from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('phase2', __name__, template_folder='../templates')

@bp.route('/canvas', methods=['GET','POST'])
def canvas():
    if request.method == 'POST':
        return redirect(url_for('phase2.themes'))
    return render_template('phase2_canvas.html')

@bp.route('/themes', methods=['GET','POST'])
def themes():
    if request.method == 'POST':
        return redirect(url_for('phase2.validate'))
    return render_template('phase2_themes.html')

@bp.route('/validate')
def validate():
    return render_template('phase2_validate.html')
