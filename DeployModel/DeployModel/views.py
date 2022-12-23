from django.shortcuts import render
import joblib
import os
from django.conf import settings


def home(req):
    return render(req, 'home.html')


def result(req):
    file_path = os.path.join(settings.FILES_DIR, 'finalized_model.sav')
    # print(file_path)
    cls = joblib.load(file_path)
    lis = []
    lis.append(req.GET['RI'])
    lis.append(req.GET['Na'])
    lis.append(req.GET['Mg'])
    lis.append(req.GET['Al'])
    lis.append(req.GET['Si'])
    lis.append(req.GET['K'])
    lis.append(req.GET['Ca'])
    lis.append(req.GET['Ba'])
    lis.append(req.GET['Fe'])
    ans = cls.predict([lis])
    return render(req, 'result.html', {'ans': ans, 'lis': lis})
