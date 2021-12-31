import os
import xmltodict
from django.http import JsonResponse
from django.shortcuts import render
from .forms import UploadFileForm
import json


from .forms import UploadFileForm


def upload_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES.get('myfile')
        if not file:
            file = request.FILES.get('file')
        if not valid_file(file):
            return JsonResponse({"invalid choice" : "file should be xml"})
        json_data = handle_uploaded_file(file)
        return JsonResponse(json.loads(json_data), safe=False)

    return render(request, "upload_page.html")


def valid_file(f):
    if not f:
        return False
    f_name = f.name
    f_name_len = len(f_name)
    if f_name_len < 5 or f_name[f_name_len-4:] != ".xml":
        return False
    return True


def handle_uploaded_file(f):
    json_data = {}
    if not f:
        return json_data

    with open('temp.xml', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open("temp.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()
    json_data = json.dumps(data_dict)

    if os.path.exists("temp.xml"):
        os.remove("temp.xml")
    return json_data
