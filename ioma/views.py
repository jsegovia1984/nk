
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS


def export_pdf(request, queryset):
    """Generate pdf."""
     # Model data
    Fecha = format_fecha()
   
       # Numero_id_causa = causa.pedido_id # Guardo el id de la Causa (Inline) que hace referencia al ID del pedido 
     # #    causa.save()     css_file = 'pedidos_de_causas/static/ccs/style.css'


    html_string = render_to_string('report/informe.html', {'context': context})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True);
    file_name =  Fecha + '.pdf'

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'attachment; filename=' + file_name 
    response['Content-Transfer-Encoding'] = 'binary'

    response.write(result)

    return response

