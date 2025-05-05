from flask import Blueprint, render_template, request, send_file
from reportlab.pdfgen import canvas
from openpyxl import Workbook
import io, os
from datetime import datetime

bp = Blueprint('phase4', __name__, template_folder='../templates')

@bp.route('/', methods=['GET','POST'])
def summary():
    if request.method == 'POST':
        fmt = request.form.get('format')
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        if fmt == 'pdf':
            buf = io.BytesIO()
            c = canvas.Canvas(buf)
            c.drawString(100, 800, "Sustainability Report")
            c.save()
            buf.seek(0)
            return send_file(buf, download_name=f'report_{now}.pdf', as_attachment=True)
        else:
            path = f"reports/report_{now}.xlsx"
            wb = Workbook()
            wb.save(path)
            return send_file(path, as_attachment=True)
    return render_template('phase4_report.html')
