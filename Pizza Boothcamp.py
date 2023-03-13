#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:24:32 2023

@author: buseeken
"""
import csv
import datetime


class Pizza():
    def __init__(self, name, description, price):
        self.name=name
        self.description=description
        self.price=price
        
class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita\", \"Tomato sauce, mozeralla, basil", 135.00)
        
class TürkPizzası(Pizza):
    def _init__(self):
        super().__init__("Türk Pizzası\", \"Tomato sauce, sucuk, kavurma, cheese", 200.00)
        
class Dominos(Pizza):
    def _init__(self):
        super().__init__("Dominos\", \"Tomato sauce, sausage, mushroom, cheese", 185.00)

class Sade(Pizza):
    def __init__(self):
        super().__init__("Sade\", \"Tomato sauce, cheese", 100.00)



class Ingredient:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class Cheddar(Ingredient):
    def __init__(self):
        super().__init__("\Cheddar", 15.00)
    
class Olives(Ingredient):
    def __init__(self):
        super().__init__("\Olives", 5.00)

class Mushroom(Ingredient):
    def __init__(self):
        super().__init__("\Mushroom", 10.00)

class Sausage(Ingredient):
    def __init__(self):
        super().__init__("\Sausage", 20.00)
        
        
def display_menu():
    print(\"Welcome to the Pizza Place!")
    print(\"These are out pizza options:)
    print(\"1-Margherita: Tomato sauce, mozeralla, basil", 135.00)
    print(\"2-Türk Pizzası: Tomato sauce, sucuk, kavurma, cheese", 200.00)
    print(\"3-Dominos: Tomato sauce, sausage, mushroom, cheese", 185.00)
    print(\"4-Sade: Tomato sauce, cheese", 100.00)
    
    pizza_choice=input(\"Please select a pizza by entering number: \")
                      
    if pizza_choice == "1":
       pizza = Margherita()
    elif pizza_choice == "2":
       pizza = TürkPizzası()
    elif pizza_choice == "3":
       pizza = Dominos()
    elif pizza_choice == "4":
       pizza = Sade()
    else:
        print("Invalid selection")
        return
   
    print(\"These are the extra ingredients:")
    
    print(\"1-Olives - 5.00₺")
    print(\"2-Cheddar - 15.00₺")
    print(\"3-Mushroom - 10.00₺")
    print(\"4-Sausage - 20.00₺")
    
    extras_choice = input(\"Do you want to add extra ingredient? (y/n)")
    
    if extras_choice.lower() == "y" :
        extras == []:
        while True
            extra_choice = input(\"Please select an extra or enter 'done' if you do not want any extra: ")
            if extra_choice = "1":
                extras.appent(Olives())
            elif extra_choice = "2":
                extras.appent(Cheddar())
            elif extra_choice = "3":
                extras.appent(Mushroom())
            elif extra_choice = "4":
                extras.appent(Sausage())
            elif extra_choice.lower = "done":
                break 
            else:
                print("Invalid selection!")
    else:
        extras = []
    return pizza, extras
        


   def collect_information():
       customer_id = input("Enter your customer ID: ")
       customer_name = input("Enter your name: ")
       print("Enter your credit card information:")
       credit_card_number = input("Credit card number:")
       credit_card_password = input("Credit card password")
       
       return customer_id, customer_name, credit_card_number, credit_card_password
   
    
   def collect_information(pizza, extras, total_price):
       customer_id = input("Enter your customer ID: ")
       customer_name = input("Enter your name: ")
       credit_card_number = input("Enter your credit card number:")
       credit_card_password = input("Enter your credit card password")
       order_description = {pizza.name} pizza with 
       for extra in extras:
           order_description += {extra.name}
       order_description = order.description.rstrip(\", \")
       order_time = datetime.now().strftime(\"%Y-&M-&D %H:%M:%S")
       
       with open(\"Orders_Database.csv\", \"a", newline=\"\") as file:
            writer = csv.writer(file)
            writer.writerow([customer_id, customer_name, credit_card_number, credit_card_password, order_description, total_price, order_time])
            
            
    print("Thank you for your order!")
      

    
        
        
    
       
      
    
    
                       
                
    
    
    

        
        
                         
        