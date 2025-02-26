text = input("Enter a string: ")

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_pos = []
vowel_char = []

index = 0
while index < len(text):  
    char = text[index]
    if char in vowels:  
        vowel_pos.append(index)
        vowel_char.append(char)
    index += 1

vowel_char.reverse() 
text_list = list(text)

i = 0
while i < len(vowel_pos):
    pos = vowel_pos[i]  
    text_list[pos] = vowel_char[i]  
    i += 1

mod_text = "".join(text_list)
print(mod_text)
