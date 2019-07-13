# reading whole file at a time
# lines at a time using list
# writing line by line / whole 






fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('Another sample line\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()