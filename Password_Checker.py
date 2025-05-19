# Get the user's password
pass = input("Enter your password.")

def main():
  # Assign variables for each requirement
  upper_chars = False
  lower_chars = False
  digits = False
  special = False

  # Make a list of special characters to reference to
  special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
  
  # Check for uppercase, lowercase, numbers, and a special character
  for char in pass
