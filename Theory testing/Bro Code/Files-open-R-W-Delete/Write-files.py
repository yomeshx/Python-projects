import os
os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\Files-open-R-W-Delete")


sample_text = "\nDid you bitches watched the match yesterday ???"
sample_text2 = "\nWe did won the match tho"
with open("rw-test.txt","w") as txt_file: #you can give 'r' for read and 'w' for write and 'a' for append with  "," after the name or path of the text file
                                            #'w' will make a file if theres no existing file
    txt_file.write("Yooo\n whats up homie \n what are u doing ?")
    txt_file.write(sample_text)

with open("rw-test.txt","a") as txt_file: #append doing the same thing when you writing to the same file for the 2nd time does
    txt_file.write(sample_text2)