m_box = open("D:\P\Programing\Python\My Learning Projects\Test Projects\Read Massege box and get emails\mbox.txt")
for line in m_box:
    line=line.rstrip()
    sp_line = line.split() 
    if len(sp_line) < 3  or sp_line[0] != "From" : #Guardian
        continue
    print(sp_line[2])