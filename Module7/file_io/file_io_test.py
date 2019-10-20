f = open('testscores.txt', 'w')
f.write("First line")
input_list = ['1', '3', '5']
f.writelines(input_list)
f.close()
