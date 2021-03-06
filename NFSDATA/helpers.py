from .models import *

def week_day_sales(user_model,user_date=None):
    if user_date==None:
        sold_products = user_model.objects.all()
    else:
        sold_products = user_model.objects.filter(added_date=user_date)
    total_sold_yesterday = 0.0 
    total_profit_yesterday = 0.0    
    
    for item in sold_products:
        total_sold_yesterday = total_sold_yesterday + item.total_on_each_item()
        total_profit_yesterday = total_profit_yesterday + item.total_profit_or_loss()
        
    return total_sold_yesterday,total_profit_yesterday

    
def find_item_n_amount(mymodel,user_date=None,list_return=None):
    
    if user_date==None:
        sold_products = mymodel.objects.all()
    else:
        sold_products = mymodel.objects.filter(added_date = user_date)
        
    product_ids_in_set = set()
            
    for item in sold_products:
        product_ids_in_set.add(item.product_sold.id)
        
    product_amount_sold_in_day = {}
    for id in product_ids_in_set:
        amt_sold = 0
        for item in sold_products:
            if id == item.product_sold.id:
                amt_sold = amt_sold + item.product_amount_sold
        product_amount_sold_in_day[id] = amt_sold

    most_sold_item = None
    most_sold_item_amount = 0
    
    
    
    for key,value in product_amount_sold_in_day.items():
        if most_sold_item_amount < value:
            most_sold_item = Products.objects.get(id=key)
            most_sold_item_amount = value
            
    if list_return == None:
        
        return most_sold_item,most_sold_item_amount
    else:
        sorted_product_amount_sold = dict(sorted(product_amount_sold_in_day.items(),key = lambda kv:kv[1]))

        dict_len = len(sorted_product_amount_sold)
        list_key = list(sorted_product_amount_sold)
        
        for item in list_key[:dict_len-list_return]:
            sorted_product_amount_sold.pop(item)
        
        most_sold_item_list = {}
        
        for key,value in sorted_product_amount_sold.items():
            most_sold_item_list[Products.objects.get(id=key)] = value

        print(most_sold_item_list)
        return most_sold_item_list
    


def most_expensive_costly():
    expensive_item = None
    costly_item = None 
    expensive_item_cost = 0
    costly_item_cost = 1201010
      
    product = Products.objects.all()
    
    for item in product:
        if expensive_item_cost < item.product_cost_price:
            expensive_item_cost = item.product_cost_price
            expensive_item = item
            
        if costly_item_cost > item.product_cost_price:
            costly_item_cost = item.product_cost_price
            costly_item = item
            
    
    return expensive_item,costly_item 
        
    


def total_item(modelgiven, attributes,user_date=None):
    if user_date==None:
        product = modelgiven.objects.all()
    else:
        product = modelgiven.objects.filter(added_date = user_date)
    total_item = 0
    for item in product:
        total_item = total_item + getattr(item, attributes)
    
    return total_item

def total_sold_cost(modelgiven):
    product = modelgiven.objects.all()
    total_cost = 0
    for item in product:
        total_cost = total_cost + item.total_on_each_item()
    return total_cost

def total_rem_cost(modelgiven):
    product = modelgiven.objects.all()
    total_cost = 0
    for item in product:
        total_cost = total_cost + item.cost_item()
    return total_cost 
    

def seven_back_days_generator():
    from datetime import timedelta,date
    seven_day_starting_today = []
    labels = []
    for i in range(7):
        seven_day_starting_today.append(date.today() - timedelta(i))
    for i in seven_day_starting_today:
        labels.append(i.strftime("%a"))
        
    return seven_day_starting_today,labels
 
 


def most_profit_given():
    products = SoldProducts.objects.all()
    profit_earned = {}
    idsset = set()
    for item in products:
        idsset.add(item.product_sold.id)
    
    for id in idsset:
        total_profit = 0
        for item in products:
            if item.product_sold.id == id:
                total_profit = total_profit + item.total_profit_or_loss()
        profit_earned[id] = total_profit
    
    highest_profit = 0
    item = None
    
    for key,value in profit_earned.items():
        if highest_profit < value:
            highest_profit = value
            item = Products.objects.get(id=key)
                    
    return item.product_name,highest_profit
