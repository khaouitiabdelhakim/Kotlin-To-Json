f = open("surah_data.txt", "r",encoding="utf-8")
g = open("surah_data_json.txt", "w",encoding="utf-8")

i = 0

for line in f:
    if i == 0:
        g.write("[\n")
        i +=1
    else:
        if "Surah(" in line:
            g.write("{\n")
        elif "arrayOf(" in line:
            g.write("verses : [")
        elif "))" in line:
            g.write("]},\n")
        else:
            line = line.replace("=", ":")
            g.write(line)

f.close()
g.close()

            
    