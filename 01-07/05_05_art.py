from art import *
import lorem

style = "dotmatrix" # find more setting in art_param.py

text = lorem.text()

result = text2art(text, font=style)
print(result)