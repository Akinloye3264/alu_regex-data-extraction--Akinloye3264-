import re


#Email validation
def email_validation(email):
    pattern= r'[A-Za-z0-9-_.]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}'
    return bool(re.match(pattern, email))

#Url validation
def url_validation(url):
     pattern = r'https?:\/\/[A-Za-z0-9.-]+(?:\.[A-Za-z]{2,})(?:\/[^\s]*)?'
     return bool(re.match(pattern, url))

#phone number validation
def Phone_number_validation(phone_number):
     patterns = [
        r'\(?\d{3}\)?[ .-]?\d{3}[.-]?\d{5}',
        r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    ]
     return any(bool(re.match(p, phone_number)) for p in patterns)

#credit card validation
def credit_card_validation(credit_card):
    patterns = [
        r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}',
        r'^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}$'
    ]
    return any(bool(re.match(p, credit_card)) for p in patterns)

# time validation
def time_validation(time):
      patterns = [
        r'\d{1,}[:]\d{2}[ ]?([a-zA-Z]+)?',
        r'([0-9]+):[0-5][0-9] ?([APMapm]{2})?',
        r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]([ a-zA-Z]+)?'
    ]
      return any(bool(re.match(p, time)) for p in patterns)


#Html tag validation
def html_tag_validation(html_tags):
      patterns = [
        r'<[^>]+>',
        r'<\s*[a-zA-Z]+(?:\s+[^>]+)?>',
        r'^\<[a-zA-Z0-9 =."]+\>$'
    ]
      return any(bool(re.match(p, html_tags)) for p in patterns)

# hashtag validation
def hashtag_validation(tags):
        patterns = [
        r'#[A-Za-z0-9_]+',
        r'#\w+'
    ]
        return any(bool(re.match(p, tags)) for p in patterns)

# currency validation
def currency_validation(currency):
     pattern = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'
     return bool(re.match(pattern, currency))


# function to ask for an id to validate
def validation():
     print("""
             1. Email
             2. Url
             3. phone number
             4. credit card
             5. Time
             6. Html tag
             7. hash tag
             8. currency
             """)
     choice = input("Enter your choice from (1-8): ")


     if choice == '1':
        email = input("Enter an email to validate: ")
        print("Valid Email" if email_validation(email) else "Invalid Email")

     elif choice == '2':
      url = input("Enter a URL to validate: ")
      print("Valid URL" if url_validation(url) else "Invalid URL")

     elif choice == '3':
        phone_number = input("Enter a phone number to validate: ")
        print("Valid Phone Number" if Phone_number_validation(phone_number) else "Invalid Phone Number")

     elif choice == '4':
        credit_card = input("Enter a credit card number to validate: ")
        print("Valid Credit Card" if credit_card_validation(credit_card) else "Invalid Credit Card")

     elif choice == '5':
        time = input("Enter a time to validate: ")
        print("Valid Time" if time_validation(time) else "Invalid Time")

     elif choice == '6':
        html_tag = input("Enter an HTML tag to validate: ")
        print("Valid HTML Tag" if html_tag_validation(html_tag) else "Invalid HTML Tag")

     elif choice == '7':
        tag = input("Enter a hashtag to validate: ")
        print("Valid Hashtag" if hashtag_validation(tag) else "Invalid Hashtag")

     elif choice == '8':
        currency = input("Enter a currency amount to validate: ")
        print("Valid Currency" if currency_validation(currency) else "Invalid Currency")

     else:
        print("Invalid choice. Please select a number between 1 and 8.")
# main function to run the program
if __name__ == "__main__":
    while True:
        validation()
        another = input("Do you want to validate another? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    print("Thank you for using the validator! Goodbye👋!")
