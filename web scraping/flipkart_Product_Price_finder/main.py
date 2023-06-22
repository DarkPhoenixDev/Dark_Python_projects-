from bs4 import BeautifulSoup 
import requests
from smtplib import SMTP
from email.mime.text import MIMEText

# Create the message

# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# ##CREATE DATABASE
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# #Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# with app.app_context():
#     class Prices(db.Model):
#         Product_Title = db.Column(db.String(500),unique=True)
#         Product_Price = db.Column(db.Integer)
#     db.create_all()

url = f"https://www.flipkart.com/nothing-phone-1-black-256-gb/p/itmeea53a564de47?pid=MOBGCYGPWXYRRNB4&lid=LSTMOBGCYGPWXYRRNB426WTZ8&marketplace=FLIPKART&q=nothing&store=search.flipkart.com&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=38139327-cf91-49ba-8619-e68345d8428d.MOBGCYGPWXYRRNB4.SEARCH&ppt=sp&ppn=sp&ssid=urkztzo4mo0000001681403426348&qH=3e47b75000b0924b"

response = requests.get(url=url).text
soup = BeautifulSoup(response, "html.parser")
Product_Title = soup.find(name="span",attrs={"class" : "B_NuCI"}).text
Product_Price =  soup.find(name="div",attrs={"class" : "dyC4hf"}).text
Product_Price = str(Product_Price).split("₹")
Product_Price = "₹" + Product_Price[1]
# Price = Prices(
#     Product_Title = Product_Title,
#     Product_Price = Product_Price
# )
# db.session.add(Price)
# db.session.commit()
USERNAME = "zhackerx3@gmail.com"
PASSWORD = "fzsiksvtnsfdajjm"
print(f"Product Price: {Product_Price} \nProduct_Title: {Product_Title}")
current_price = input("Enter the current Price:")
if Product_Price < current_price:
   msg = MIMEText(f"Hey! Prince The product you looking for now get discount the Price of Product is not :{current_price} it is now:{Product_Price}", 'plain', 'utf-8')
   connection = SMTP("smtp.gmail.com",587)
   connection.starttls()
   connection.login(USERNAME,PASSWORD)
   connection.sendmail(from_addr=USERNAME,to_addrs="pv8920034911@gmail.com",msg=msg.as_string())
