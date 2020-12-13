import os
import shutil
import pandas as pd
import pdfkit

from django.http import FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from PersonalDjangoTutorial.settings import BASE_DIR


def index(request):
    return render(request, 'index.html')


def no_found(requests):
    return render(requests, '404.html')


@csrf_protect
def downloads(request, dir_path=None):
    path = os.path.join(BASE_DIR, 'downloads')
    if request.method == "GET":
        if request.GET['path']:
            dir_path = request.GET['path']
    if dir_path:
        path = os.path.join(path, dir_path)
    file = os.listdir(path)
    files = list()
    folder = list()
    for i in file:
        if os.path.isdir(os.path.join(path, i)):
            temp = os.path.join(path, i).split(os.path.join(BASE_DIR, 'downloads'))[-1]
            folder.append({'name': i,
                           'value': temp,
                           'dir_path': '?path=' + temp.split('/', 1)[-1]
                           })
            continue
        size = os.path.getsize(os.path.join(path, i))
        if 2**20 > size:
            size = "%.2fkB" % (size / float(2**10))
        elif 2**30 > size >= 2**20:
            size = "%.2fMB" % (size / float(2**20))
        elif size >= 2**30:
            size = "%.2fGB" % (size / float(2**30))
        files.append({"name": i,
                      'url': dir_path + '/' + i if dir_path else i,
                      'size': size
                      })
    if request.method == "POST":
        for i in request.POST:
            temp = os.path.join(BASE_DIR, i)
            if os.path.exists(temp):
                if os.path.isfile(temp):
                    os.remove(temp)
                elif os.path.isdir(temp):
                    shutil.rmtree(temp)

        request.method = 'GET'
        return downloads(request)
    return render(request, "downloads.html", {"files": files, 'folder': folder})


@csrf_protect
def pscp(request):
    """
    pip install pandas
    pip install pdfkit
    pip install xlrd
    当你在终端执行一个带GUI功能的程序的时候，如果DISPLAY变量没有定义，就会报相应的错误。特别是在Linux上
    tips: export QT_QPA_PLATFORM='offscreen'
    """
    if request.method == "POST":
        date = request.POST['date']
        address = request.POST["address"]
        if request.FILES and request.FILES["file"]:
            if not os.path.exists(os.path.join(BASE_DIR, 'cache')):
                os.mkdir(os.path.join(BASE_DIR, 'cache'))
            dir_path = os.path.join(BASE_DIR, 'cache')
            with open(dir_path + "/pdf.xls", 'wb+') as destination:
                for chunk in request.FILES["file"].chunks():
                    destination.write(chunk)
            data = pd.read_excel(os.path.join(dir_path, "pdf.xls"))
            users = list()
            length = len(data)
            n = length // 4 if length % 4 == 0 else length // 4 + 1
            for i in range(n):
                for j in range(4):
                    if j * n + i >= length:
                        continue
                    users.append({"name": data.iloc[j * n + i][0],
                                  "sex": data.iloc[j * n + i][1],
                                  "id": data.iloc[j * n + i][4],
                                  "front": str(data.iloc[j * n + i][3])[:-4],
                                  "rear": str(data.iloc[j * n + i][3])[-4:],
                                  "workings": data.iloc[j * n + i][8],
                                  "time": data.iloc[j * n + i][6]})

            options = {
                'page-size': 'A4',
                'margin-top': '0in',
                'margin-left': '0in',
                'margin-bottom': '0in',
                'margin-right': '0in',
                'page-height': '297mm',
                'page-width': '210mm',
                'encoding': "UTF-8",
                'custom-header': [
                    ('Accept-Encoding', 'gzip')
                ],
                'no-outline': None,
                'quiet': None
            }
            html = render(request, "pscp2.html", {'users': users, "date": date, "address": address}).content
            pdfkit.from_string(str(html, encoding='utf-8'), dir_path + "/pdf.pdf", options=options)
            return FileResponse(open(os.path.join(dir_path, "pdf.pdf"), 'rb'), content_type='application/pdf')
    else:
        return render(request, 'pscp.html')
