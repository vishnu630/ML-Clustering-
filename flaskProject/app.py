import model
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    real_class = model.real_class()
    kmeans_Cluster = model.kmeans_Cluster()
    kaccuracy, kconfusion = kmeans_Cluster
    gmmaccuracy,gmmConfusionmatrix=model.gmm_Cluster()
    print(gmmaccuracy),print(gmmConfusionmatrix)
    return render_template('index.html',a=gmmaccuracy,b=gmmConfusionmatrix,c=kaccuracy,d=kconfusion)


if __name__ == '__main__':
    app.run()
