import re, shutil, os  # re — module for regular expressions (pattern search in text)
           # json — module for working with JSON data format 
def parse_check() -> list:   # function definition; returns a list
    with open("raw.txt", "r", encoding="UTF-8") as f:  
        # open() — opens file "raw.txt"
        # "r" — read mode
        # encoding="UTF-8" — text encoding standard
        txt = f.read()   # read() — reads the entire file content as one string

    result = {}   # dictionary initialization (later replaced by list)

    product_info = re.findall(r"^\d+\.\n(.+)\n(.+)\n(.+)", txt, re.MULTILINE)
    # re.findall() — finds all matches of regex in the text
    # ^ — start of line
    # \d+ — one or more digits
    # \. — literal dot
    # \n — newline
    # (.+) — capturing group; any characters until newline
    # re.MULTILINE — allows ^ to match at the start of every line
    # returns tuples containing product name, unit price info, total price

    print("Check info")   # prints title
    print("=" * 145)   # prints separator line

    print(f'{"id":5} {"Product Name: ":100} {"Product Price":10}')
    # f-string — formatted string output
    # :5 , :100 , :10 — field width formatting

    print("-" * 145)   # visual separator

    id = 1   # product counter
    result = []   # list initialization to store parsed product data

    for product in product_info:   # loop through each product tuple
        product_name = product[0]   # first element → product name

        product_unit_price_info = product[1]   
        # second element → quantity and unit price text

        product_quantity = (product_unit_price_info.split(" x "))[0]
        # split() — splits string by delimiter " x "
        # [0] — quantity

        product_unit_price = (product_unit_price_info.split(" x "))[1]
        # [1] — unit price

        product_price = product[2]   # third element → total price

        print(f"{id}.    {product_name:100} {product_price:10}")
        # formatted output of product table row

        product_dict_info = {
            "product_id": id,              # dictionary key-value pair
            "product_name": product_name,
            "product_unitprice": product_unit_price,
            "product_quantity": product_quantity,
            "total_price": product_price
        }

        result.append(product_dict_info)
        # append() — adds dictionary to the list

        id += 1   # increment product counter

    print("-" * 145)

    total_amount = re.findall(r"^ИТОГО:\n(.+)", txt, re.M)
    # finds total amount
    # ИТОГО — Russian word meaning "TOTAL"
    # re.M — same as re.MULTILINE

    payment_method = re.findall(r"^(.*)\n(.+)\nИТОГО", txt, re.M)
    # finds payment method text before the "TOTAL" section

    date = re.findall(r"^Время: (.+)", txt, re.M)
    # finds date line beginning with "Время:" (Time)

    final_payment_method = payment_method[0][0][0:-1]
    # extracts payment method string
    # [0][0] — accesses first tuple and first element
    # [0:-1] — removes last character

    result.append(f"payment_method: {final_payment_method}")
    # adds payment method string to result list

    print(f"Payment method: {final_payment_method}")

    result.append(f"check_date: {date[0]}")
    # adds date information to result list

    print(f"Date: {date[0]}")

    result.append(f"Total: {total_amount[0]}")
    # adds total amount to result list

    print(f"Total: {total_amount[0]}")

    return result   # returns parsed receipt data


a = parse_check()   # function call; executes receipt parsing

# parsed_data = json.dumps(a, separators = (",", ":"))
# json.dumps() — converts Python object into JSON string
# separators — removes extra spaces in JSON formatting

# print("\n", *a, sep = "\n")
# prints each element of the list on a new line

# print("\n", parsed_data)
# prints JSON formatted output