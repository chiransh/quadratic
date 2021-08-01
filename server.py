from flask import Flask
from matplotlib.figure import Figure
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
# from flask_restful import Api

app=Flask(__name__)
# api=Api(app)

app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure(a=1,b=1,c=1):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x = np.linspace(-10, 10, 1000)
    y = a*x*x + b*x + c
    axis.plot(x, y)
    return fig
    
app.run()
