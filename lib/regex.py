import re

# Regular expression for validating names
name = r"^[A-Z][a-z]*(?:'[A-Za-z]+)?(?: [A-Z][a-z]*(?:-[A-Z][a-z]*)?)*$"
name_regex = re.compile(name)

# Regular expression for validating phone numbers
phone_number = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# Regular expression for validating email addresses
# Ensures the email starts with a letter
email_address = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
