from flask import Flask, render_template,request,redirect
from pgfunc import fetch_data,insert_products


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
   prods = fetch_data("products")
   return render_template('products.html', products=prods)

@app.route("/sales")
def sales():
   sales = fetch_data("sales")
   return render_template('sales.html', sales=sales)

@app.route('/addproduct', methods =["POST","GET"])
def addproducts():
   name=request.form["name"]
   buying_price=request.form["buying_price"]
   selling_price=request.form["selling_price"]
   stock_quantity=request.form["stock_quantity"]
   print(name)
   print(buying_price)
   print(selling_price)
   print(stock_quantity)
   product=(name,buying_price,selling_price,stock_quantity)
   insert_products(product)
   return redirect("/products")


# if___name___ =="__main__":
app.run()







# Create an object called app
# __name__ is used to tell Flask where to access HTML Files
# All HTML files are put inside "templates" folder
# All CSS/JS/ Images are put inside "static" folder

# a route is an extension of url which loads you a html page
# @ - a decorator(its in-built ) make something be static
