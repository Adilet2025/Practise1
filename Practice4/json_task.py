import json                         # import json module to work with JSON files

print("=" * 80)                     # print 80 "=" symbols (top line)

print(f"{'DN':50} {'Description':15} {'Speed':7} {'MTU':5}")  
# print table header with fixed column width

print("-" * 80)                     # print 80 "-" symbols (line under header)


with open("sample-data.json", "r") as json_file:  
    # open JSON file in read mode ("r")

    parsed_data = json.load(json_file)  
    # read JSON file and convert to Python dictionary


data = parsed_data["imdata"]        
# take "imdata" part from dictionary (it is a list)


count = 1                           
# create counter variable


for part in data:                   
    # loop through each element in list

    if count <= 3:                  
        # check if we printed less than 3 rows

        inner_data = part["l1PhysIf"]  
        # get "l1PhysIf" dictionary

        attr = inner_data["attributes"]  
        # get "attributes" dictionary

        dn = attr.get("dn", "")      
        # get "dn" value, if not exist return empty string

        description = attr.get("descr", "")  
        # get description value

        speed = attr.get("speed", "")  
        # get speed value

        mtu = attr.get("mtu", "")    
        # get mtu value

        print(f"{dn:50} {description:15} {speed:7} {mtu:5}")  
        # print values in table format

        count += 1                  
        # increase counter by 1

    else:
        break                       
        # stop loop after 3 rows

# JSON (JavaScript Object Notation) is a text format to store and send data.
# It uses key–value pairs.
# Why do we use JSON?

# It is simple text

# It is easy to read

# It works in many languages (Python, JavaScript, Java)

# It is good for structured data