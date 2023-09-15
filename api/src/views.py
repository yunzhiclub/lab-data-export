import os
import shutil

from django.http import HttpResponse
from tute.main import start
from zipfile import ZipFile

def upload(request):
    file = request.FILES['file']
    try:
        error, logs, files = start(file)
    except BaseException as e:
        print(str(e))
        response = HttpResponse(str(e), content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format('error.txt')
        return response

    if error is True:
        response = HttpResponse(logs, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format('error.txt')
        for file in files:
            os.remove(file)
        return response
    else:
        response = HttpResponse(content_type='application/zip')
        with ZipFile(response, 'w') as myzip:
            for file in files:
                shutil.move(file, os.path.basename(file))
                myzip.write(os.path.basename(file))
                os.remove(os.path.basename(file))
        myzip.close()
        response['Content-Disposition'] = 'attachment; filename={0}'.format('tute-pj-dbf.zip')
        return response
