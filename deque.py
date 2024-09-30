from collections import deque

def is_palindrom(text):
    # Create deque
    d = deque()
    # Remove spaces
    text = text.replace(' ', '')
    # Lower text
    text = text.lower()
    # Add each char to deque
    for char in text:
        d.append(char)
    # Reverse chars in deque
    d.reverse()
    # Create string from reversed chars
    reversed_text = ''.join(d)
    # Compare original text with reversed
    return text == reversed_text
    

print(is_palindrom('abcgcbal'))