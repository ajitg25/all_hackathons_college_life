f = open('readme.txt', 'w')
with open('readme.txt', 'w') as f:
    f.write('readme')



f.write('\n')
f.writelines('\n')

lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.writelines(lines)