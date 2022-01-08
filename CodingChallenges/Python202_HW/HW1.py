'''
     Pass in a dictionary to a function 
     Validate price variable as a float or an int
'''

def has_valid_price(price_dict):
    #if price_dict.has_key('product'):
    if price_dict == None:
        return False
    if "product" in price_dict:
       # print("Key found")
        price_key_name = "price"

        if price_dict[price_key_name]>=0:
        
            if type(price_dict[price_key_name]) == float or type(price_dict[price_key_name]) == int:
                return True
            else:
                return False
        #elif price_dict[price_key_name] == 0:
            #print(price_dict["product"], "has no cost")
        else:
            return False
    else:
        return False

    # for key in price_dict:
    #     if (type(price_dict[key])) == float:
    #         print("key: ", key,", value: ", price_dict[key], "is a float")
    #     elif (type(price_dict[key])) == int:
    #         print("key: ", key,", value: ", price_dict[key], "is an int")

def main():
    # D = {'price1': 20.00, 'price2': 5, 'price3': 12.75}
    print(has_valid_price({"product":"Milk", "price":1.50}))
    print(has_valid_price({"product":"Cheese", "price":-1}))
    print(has_valid_price({"product":"Eggs", "price":0}))
    print(has_valid_price({"product":"Cereals", "price":3.0}))
    print(has_valid_price(None))



if __name__ == "__main__":
    main()