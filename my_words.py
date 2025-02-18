def first_letter(word):
    if not word or not isinstance(word, str):
        raise ValueError("Input must be a non-empty string")
    return word[0]
def print_middle_letter(word):
    
    if not isinstance(word, str):
        print("Error: Input must be a string.")
        return  

    word = word.strip()  
    length = len(word)

    if length == 0:
        print("Error: Input string cannot be empty.")
        return

    middle_index = length // 2  

    if length % 2 == 0:  
        print(word[middle_index - 1:middle_index + 1])  
    else: 
        print(word[middle_index])  