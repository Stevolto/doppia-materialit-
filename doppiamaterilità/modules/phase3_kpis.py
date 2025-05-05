from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('phase3', __name__, template_folder='../templates')

kpi_list = {
    "GRI": [{"code":"GRI 305-1","desc":"Direct GHG emissions"}],
    "ESRS": [{"code":"ESRS E1","desc":"Climate mitigation"}]
}

@bp.route('/', methods=['GET','POST'])
def select_standard():
    if request.method == 'POST':
        std = request.form.get('standard')
        return redirect(url_for('phase3.choose_kpis', standard=std))
    return render_template('phase3_select.html')

@bp.route('/kpis/<standard>', methods=['GET','POST'])
def choose_kpis(standard):
    kpis = kpi_list.get(standard, [])
    if request.method == 'POST':
        selected = request.form.getlist('kpis')
        return render_template('phase3_confirmation.html', standard=standard, selected=selected)
    return render_template('phase3_select.html', standard=standard, kpis=kpis)
