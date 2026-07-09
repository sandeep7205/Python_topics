import re

# Define a string that contains email addresses
text = "Please contact us at support@example.com or sales@example.net"

# Define a regular expression pattern for matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Use the findall method to find all occurrences of the pattern
email_addresses = re.findall(email_pattern, text)

# Print out the list of found email addresses
print(email_addresses)
