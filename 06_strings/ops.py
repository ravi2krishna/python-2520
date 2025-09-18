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

