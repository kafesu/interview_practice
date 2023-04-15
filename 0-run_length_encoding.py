def encode(text=""):
    encoded_text = ""
    
    if len(text) != 0:
        previous_char = text[0]
        count = 0
        
        for current_char in text:
            if current_char != previous_char:
                encoded_text += f'{count}{previous_char}'
                count = 1
            else:
                count += 1
            previous_char = current_char
        
        encoded_text += f'{count}{previous_char}'
    
    return encoded_text


def decode(text=""):
    decoded_text = ""
    number = ""
    
    for char in text:
        try:
            int(char)
            number += char
        except:
            decoded_text += char * int(number)
            number = ""
    
    return decoded_text

encoded_text = encode("A")
print(encoded_text)

decoded_text = decode(encoded_text)
print(decoded_text)
