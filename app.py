from flask import Flask

app = Flask(__name__)


@app.route('/')
def mainAction():
    return '<a href="/catalog">catalog</a>'


@app.route('/catalog')
def catalogAction():
    return convertProductsListToDictionary(getProducts())


@app.route('/catalog/<name>')
def catalogOneAction(name):
    productsDic = convertProductsListToDictionary(getProducts())

    return productsDic[name]


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
