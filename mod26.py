# Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}
# we are using ROT13 to encrypt the message
#ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet.

rot13_list=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
rot13_list_converted= ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

word_to_convert="cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX"

for letter in word_to_convert:
    if letter in rot13_list:
        index=rot13_list.index(letter)
        print(rot13_list_converted[index], end="")
    else:
        print(letter, end="")