from django.shortcuts import render
from django.conf import settings
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

def home(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)
        # Realizar los cálculos y predicciones necesarias
        # Utilizar LinearRegression y r2_score de scikit-learn

        # Ejemplo de cálculo de R2
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        r2 = r2_score(y, predictions)

        return render(request, 'result.html', {'r2': r2})
    return render(request, 'home.html')
