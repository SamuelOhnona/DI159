matrix = [
    ["7", "i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

def decrypt_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    decoded_message = []
    
    # read every col from top to bottom
    for col in range(cols):
        for row in range(rows):
            char = matrix[row][col]
            decoded_message.append(char)
    
    # Conserve only letters and change sequencies by letter
    import re
    message = "".join(decoded_message)
    cleaned_message = re.sub(r'[^a-zA-Z]+', ' ', message)  # Replace no letters by space
    
    return cleaned_message.strip()

# Decrypt
secret_message = decrypt_matrix(matrix)
print(secret_message)