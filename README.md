# Regular Expression Validator

This Python script, `regex.py`, provides a command-line interface for validating various data formats using regular expressions. It includes validation for email addresses, URLs, phone numbers, credit card numbers, time formats, HTML tags, hashtags, and currency amounts.

## Features

*   **Email Validation:** Checks if a given string is a valid email address.
*   **URL Validation:** Checks if a given string is a valid URL.
*   **Phone Number Validation:** Checks if a given string is a valid phone number.
*   **Credit Card Validation:** Checks if a given string is a valid credit card number.
*   **Time Validation:** Checks if a given string is a valid time format.
*   **HTML Tag Validation:** Checks if a given string is a valid HTML tag.
*   **Hashtag Validation:** Checks if a given string is a valid hashtag.
*   **Currency Validation:** Checks if a given string is a valid currency amount (USD).

## Requirements

*   Python 3.x
*   `re` module (built-in to Python)

## How to Use

1.  **Clone the repository (if applicable) or download the `regex.py` file.**
2.  **Open a terminal or command prompt.**
3.  **Navigate to the directory where you saved the `regex.py` file.**
4.  **Run the script using the command:** `python regex.py`
5.  **Follow the on-screen prompts to select a validation type and enter the string you want to validate.**
6.  **The script will output whether the input is valid or invalid based on the selected validation type.**
7.  **The script will ask if you want to validate another input. Type 'yes' to continue or 'no' to exit.**

## Validation Functions

The script includes the following validation functions:

*   `email_validation(email)`: Validates email addresses.
*   `url_validation(url)`: Validates URLs.
*   `Phone_number_validation(phone_number)`: Validates phone numbers.
*   `credit_card_validation(credit_card)`: Validates credit card numbers.
*   `time_validation(time)`: Validates time formats.
*   `html_tag_validation(html_tags)`: Validates HTML tags.
*   `hashtag_validation(tags)`: Validates hashtags.
*   `currency_validation(currency)`: Validates currency amounts.

Each function uses regular expressions to match the input string against a defined pattern.

## Regular Expression Patterns

The script uses the following regular expression patterns for validation:

*   **Email:** `r'[A-Za-z0-9-_.]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}'`
*   **URL:** `r'https?:\/\/[A-Za-z0-9.-]+(?:\.[A-Za-z]{2,})(?:\/[^\s]*)?'`
*   **Phone Number:**
    *   `r'\(?\d{3}\)?[ .-]?\d{3}[.-]?\d{5}'`
    *   `r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'`
*   **Credit Card:**
    *   `r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}'`
    *   `r'^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}$'`
*   **Time:**
    *    `r'\d{1,}[:]\d{2}[ ]?([a-zA-Z]+)?'`
    *    `r'([0-9]+):[0-5][0-9] ?([APMapm]{2})?'`
    *    `r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]([ a-zA-Z]+)?'`
*   **HTML Tag:**
    *   `r'<[^>]+>'`
    *   `r'<\s*[a-zA-Z]+(?:\s+[^>]+)?>'`
    *   `r'^\<[a-zA-Z0-9 =."]+\>$'`
*   **Hashtag:**
    *   `r'#[A-Za-z0-9_]+'`
    *   `r'#\w+'`
*   **Currency:** `r'\$\d{1,3}(,\d{3})*(\.\d{2})?'`

## Contributing

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

## Author

*   Oluwatimilehin

## License

This project is open source and available under the [MIT License](LICENSE).
