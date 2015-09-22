import string
pattern1=input().upper().split('.')
#pattern2=input().split('.')
valid_chars=set()
for x in string.ascii_uppercase:
    valid_chars.add(x)
for x in string.digits:
    valid_chars.add(x)

valid_chars.add('%')
valid_chars.add('*')
valid_chars.add('**')
print(valid_chars)
for element in pattern1:#, pattern2:
    print(set(element))
    if not (set(element) <= valid_chars):
        print("invalid string")
    if '*' in element:
        if element != '*' and element != '**':
            print("only valid *-containing tokens are * and **")