from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)


class Product:

    def __init__(self, item_id, slug, name, price, description, url):
        self.id = item_id
        self.slug = slug
        self.name = name
        self.price = price
        self.description = description
        self.url = url



def get_product_objects():
    products_data = get_products()
    result = []

    for product_data in products_data:
        product_object = Product(product_data['item_id'], product_data['slug'], product_data['name'],
                                 product_data['price'], product_data['url'], product_data['description'])
        result.append(product_object)

    return result


@app.route('/')
def main_view():
    return render_template('mainPage.html')


@app.route('/catalog/')
def catalog_view():
    products = get_product_objects()

    for item in products:
        item.url = url_for('catalog_one_view', slug=item.slug)

    return render_template('catalog_ilya.html', products=products)


@app.route('/catalog/<slug>')
def catalog_one_view(slug):
    product = get_product_by_slug(slug)

    if product == {}:
        return redirect(url_for('error_404_view'))

    return render_template('product.html', product=product)


def get_product_by_slug(slug):
    products = get_products()
    result = {}

    for product in products:
        if slug == product['slug']:
            result = product
            break

    return result


@app.route('/not-found')
def error_404_view():
    return render_template('error404.html')


@app.route('/stores/')
def stores_view():
    stores = get_stores()

    for store in stores:
        store['url'] = url_for('stores_one_view', slug=store['slug'])

    return render_template('store_list.html', stores=stores)


@app.route('/stores/<slug>')
def stores_one_view(slug):
    store = get_store_by_slug(slug)

    if store == {}:
        return redirect(url_for('error_404_view'))

    return render_template('store.html', store=store)


def get_store_by_slug(slug):
    stores = get_stores()
    result = {}

    for store in stores:
        if slug == store['slug']:
            result = store
            break

    return result


def get_stores():
    return [
        {
            "store_id": 1,
            "slug": 'Karavannaya',
            "name": 'Основной офис',
            "address": 'Караванная д.1'
        },
        {
            "store_id": 2,
            "slug": 'Nevsky',
            "name": 'Дополнительный офис - 1',
            "address": 'Невский д.150'
        },
        {
            "store_id": 3,
            "slug": 'Kaprskoe',
            "name": 'Дополнительный офис - 2',
            "address": 'Деревня Капрское'
        }
    ]


def get_products():
    return [
        {
            "item_id": 1,
            "slug": 'hermitage',
            "name": 'Экскурсия в Эрмитаж',
            "price": 1500,
            "description": 'Обзорная экскурсия по Эрмитажу, продолжительность 3 часа',
            "url": ''
        },
        {
         "item_id": 2,
         "slug": 'citytour',
         "name": 'Обзорная экскурсия по городу',
         "price": 2000,
         "description": 'Автобусная экскурсия по городу в сопровождении гида. Продолжительность 4 часа.',
         "url": '',
         },
        {"item_id": 3,
         "slug": 'pushkin',
         "name": 'Пушкин и Царское село',
         "price": 2500,
         "description": 'Экскурсия в Царское Село. Посещение Екатерининского дворца, Екатерининского парка и Янтарной комнаты. Продолжительность 5 часов.',
         "url": '',
         },
        {"item_id": 4,
         "slug": 'peterhof',
         "name": 'Петергоф',
         "price": 4000,
         "description": 'Экскурсия в Петергов. Посещение Большого дворца, Нижнего и Верхнего парков, Телеграфа. Продолжительность 5 часов.',
         "url": ''
         },
        {"item_id": 5,
         "name": 'Реки и Каналы',
         "slug": 'canales',
         "price": 500,
         "description": 'Обзорная экскурсия по каналам, с выходов в Неву, продолжительность 1 час',
         "url": ''
         },
    ]
