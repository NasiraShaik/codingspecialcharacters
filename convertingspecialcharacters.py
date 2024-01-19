import re

def process_string(input_string):
    # Remove numbers
    result_string = re.sub(r'\d', '', input_string)
    
    # Replace special characters with spaces
    result_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', result_string)
    
    return result_string

# Example usage:
input_str = input()
output_str = process_string(input_str)
print(output_str)