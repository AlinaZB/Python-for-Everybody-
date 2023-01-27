str = "X-DSPAM-Confidence:    0.8475"
print(str)
first = str.find('0')
piece = str[first-1:]
value = float(piece)
print(value)
