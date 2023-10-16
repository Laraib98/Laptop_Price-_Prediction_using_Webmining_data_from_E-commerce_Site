from django.shortcuts import render
import pandas as pd
import joblib
import numpy as np
# Load the saved model
pipe_loaded = joblib.load('rfmodel.joblib')

# Create your views here.


def index(request):
    return render(request, 'index.html')


def analysis(request):
    return render(request, 'analysis.html')


def predict(request):
    try:
        d = {}
        if request.method == 'POST':
            d['Company'] = [request.POST['brand'], ]

            d['TypeName'] = [request.POST['type'], ]

            ram = request.POST['ram']
            d['Ram'] = [int(ram), ]

            weight = request.POST['weight']
            d['Weight'] = [float(weight), ]

            touch = request.POST['Touchscreen']
            d['Touchscreen'] = [int(touch), ]

            ips = request.POST['IPS']
            d['Ips'] = [int(ips), ]
            d['ppi'] = [220.678, ]
            d['Cpu brand'] = [request.POST['CPU'], ]
            d['HDD'] = [int(request.POST['HDD']), ]
            d['SSD'] = [int(request.POST['SSD']), ]
            d['Gpu brand'] = [request.POST['GPU'], ]
            d['os'] = [request.POST['OS'], ]
            try:
                print(d)
                dtf = pd.DataFrame(d)

                y_pred = pipe_loaded.predict(dtf)
                print(y_pred)
                d['PREDICTION'] = np.round(np.exp(y_pred), 2)
                return render(request, 'prediction.html', {"d": d})
            except:
                print("Failed")

    except:
        pass
    return render(request, 'index.html')


def visualize(request):
    df = pd.read_csv('data.csv')

    data = df.to_dict('records')

    context = {'data': data}

    return render(request, 'display_data.html', context)
