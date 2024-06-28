# En NLP/views.py
from django.shortcuts import render
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import io
import urllib, base64

def procesamiento_nlp(request):
    # Cargar el conjunto de datos Iris
    iris = load_iris()
    
    # Crear un DataFrame con los datos de Iris
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    
    # Generar un gráfico con matplotlib
    plt.figure(figsize=(8, 6))
    plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=iris.target)
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('Scatter plot of Iris dataset')
    
    # Convertir el gráfico a imagen para mostrar en la plantilla HTML
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')

    plt.close()

    # Pasar el DataFrame y la imagen del gráfico como contexto al template HTML
    return render(request, 'procesamiento_nlp.html', {'df': df, 'graphic': graphic})
