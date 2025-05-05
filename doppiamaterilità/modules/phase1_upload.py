from flask import Blueprint, render_template, request, flash, redirect, url_for

bp = Blueprint('phase1', __name__, template_folder='../templates')

@bp.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('documento')
        if file and file.filename:
            flash('Documento caricato con successo!')
            return redirect(url_for('phase1.upload'))
    return render_template('phase1_upload.html')
