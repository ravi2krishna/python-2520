# String Methods 

# simulate gmail user id input formatting
email = input("Enter Your ID: ")
format_email = email.lower() + "@gmail.com"
print("Original Input: "+email)
print("Formatted Output: "+format_email)

# simulate PAN p » Only Alphabets or Numbers Allowed
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input("Enter Your PAN ID: ")

if pan.isalnum():
    format_pan = pan.upper()
    print("User given PAN: "+pan)
    print("Formatted PAN: "+format_pan)
else:
    print("User given PAN is invalid: "+pan)

# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png

# redirect call based on isd code
mobile_num = input("Enter Mobile Number with ISD Code: ")
if mobile_num.startswith("+91"):
    print("Calling India")
elif mobile_num.startswith("+1"):
    print("Calling USA")
elif mobile_num.startswith("+86"):
    print("Calling China")
else:
    print("Calling support available only to India, USA & China")
    
# email synchronization -> gmail.com
source_email = input("Enter Your Email ID: ")
destination_email = input("Enter Your Email ID: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("synchronizing email")
else:
    print("synchronizing failed both providers should of same type")

# gmail removes spaces at the beginning and ending of email id provided 
email = input("Enter Your Email ID: ")
format_email = email.strip()
print(format_email)

# csv / excel lot of data in rows 
# Name,City,Age,Email,Role
emp_row = "John,Hyd,25,john@gmai.com,Developer"
print("Original Data: "+emp_row)
# ['John,Hyd,25,john@gmai.com,Developer']
fields = emp_row.split(",")
# ['John', 'Hyd', '25', 'john@gmai.com', 'Developer']
print(fields)

# print emp name and role
print("Name: "+fields[0])
print("Role: "+fields[4])

# replace : order templates / otp templates 
order_template_amazon = "Hello User, your order #{order_id} has been shipped"
order_id = "AMAZON-IN-9098080"

# user_email 
user_email = order_template_amazon.replace("{order_id}",order_id)
print(user_email)
