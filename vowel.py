def get_vowels_number(text):
    vowels_number = 0
    vowels_list =["a", "e", "i", "o", "u", "y"]
    for i in range(0, len(text)):
        if text[i] in vowels_list:
            vowels_number += 1
    return vowels_number

print(get_vowels_number("Abracadabrau"))

