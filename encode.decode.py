# You are given:
# 1. A source text (input)
# 2. Alphabet (alpha = "abcdefgh....xyz")
# 3. Key (key = "qwertzuioplkjhgfdsayxcvbnm")
# len(key) == len(alpha)
# no repeating letters in alpha or key


w=int(input('Please,choose operation 1-decode or 0-encode: '))
text="Write the message: "
if w==0:
    def encode(text):
        encoded_text = ""
    # substitute all letters from the alphabet to
    # the corresponding letters in the key
        
        return encoded_text

else:
    def decode(encoded_text):
        text = ""
    # substitute all letters from the key to
    # the corresponding letters in the alphabet
        return text

# input: 0 - encode/1 - decode?
# text
# print(encoded/decoded text)#

# Hello, world! -> Itffk, dksfo!
# git stash

# Encode/decode Cyrillic letters
# Ghbdtn vbh => Привет мир
# Руддщ цщкдв => Hello world

# Optional:
# Привет мир - Privet mir
# Я робот -  Ya robot
