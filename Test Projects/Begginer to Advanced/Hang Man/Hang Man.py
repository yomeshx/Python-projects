# Game work but need more improvements!

# word = "butterfly"
# def req_ter():
#     req = input("'E' to exit or 'any key' to Continue: ").upper()
#     if req == "E":
#         quit()
# def game(word):
#     while True:
#         status = ""
#         tries = 5
#         while tries>0:
#             for l in word:
#                 ul =input("Guess a Letter : ")
#                 if ul == l:
#                     status += ul
#                     print(f"{status}    #Correct Word !")
#                 else:
#                     status += "_"
#                     print(f"{status}    #Wrong Letter!")
#             if status == word:
#                 print(f"You Win !\n     --- {status} ---")
#                 req_ter()
#                 break
#             tries -=1
#         else:
#             print("you lost")
#             req_ter()
# if __name__ =='__main__':
#     game(word)