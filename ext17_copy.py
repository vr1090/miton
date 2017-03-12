from sys import argv
from os.path import exists

#ambil parameter
print "welocome.. runing.. script from to\n"
script, path_from, path_to = argv

input_data = open(path_from).read()
file_output = open(path_to,"w")

print "menunggu...."
file_output.write(input_data)
print "selesai.."
print "pencet enter dong"
raw_input()

#closing statement
#file_output.close()
