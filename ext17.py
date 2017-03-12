file = open("ext16_doc.txt")
file_simpen = open("anjing.txt","w")
file_simpen.truncate()

isi_hati = file.read()

print ">",isi_hati

file_simpen.write("dah aku mah apa atuh")
file_simpen.close()

file.close()
