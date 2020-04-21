from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def mainAction():
    return render_template('mainPage.html')


@app.route('/catalog/')
def catalogAction():
    productsDic = convertProductsListToDictionary(getProducts())
    return render_template('catalog_ilya.html', products=productsDic)


@app.route('/catalog/<name>')
def catalogOneAction(name):
    productsDic = convertProductsListToDictionary(getProducts())
    return render_template('product.html', product=productsDic[name])


def getProducts():
    return ['COVID-19', 'H1N1', 'SARS', 'PLUGUE']


def convertProductsListToDictionary(list):
    dictinory = {}
    for number in range(len(list)):
        productID = number + 1

        product = {
            "id": productID,
            "name": list[number],
            "url": "/catalog/product_" + str(productID)
        }

        dictinory.update({'product_' + str(productID): product})
        pass

    return dictinory
