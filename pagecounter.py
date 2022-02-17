import PyPDF2
import os
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
def mzigo(request):
    # a = request.FILES['xxxx']
    file_data = request.FILES.get('xxxx')
    file_name = file_data.filename
    file_data.save(os.path.join("system","files","text", file_name))

    with open('doc.pdf', 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        a = pdf_reader.getNumPages()

        print(a)
    return HttpResponseRedirect(reverse("homepage"))
