def to_word(string):
    ans = concat_letters(*string).split("\n")
    # cut off white space at end of word.
    ans = [line[:-1] for line in ans]
    return "\n".join(ans)

def concat_letters(*letters):
    word = ["", "", "", "", ""]
    for letter in letters:
        letter = alphabet[letter].split('\n')
        for line in range(len(letter)):
            word[line] += letter[line]
    return "\n".join(word)

def expand(string, factor = 2):
    ans = ""
    for line in string.split("\n"):
        line = "".join([factor * n for n in line])
        ans += (line + "\n") * factor
    if line[-1] == '\n': line = line[:-1]
    return ans

def subs(string1, string2 = "18"):
    return string1.replace(" ", string2[0]).replace("#", string2[1])

alphabet = {
"A": """ ##  
#  # 
#### 
#  # 
#  # """,

"B": """####  
#   # 
####  
#   # 
####  """,

"C": """ ### 
#    
#    
#    
 ### """,

"D": """###  
#  # 
#  # 
#  # 
###  """,

"E": """#### 
#    
###  
#    
#### """,

"F": """#### 
#    
###  
#    
#    """,

"G": """ ###  
#     
#  ## 
#   # 
 ###  """,

"H": """#  # 
#  # 
#### 
#  # 
#  # """,

"I": """### 
 #  
 #  
 #  
### """,

"J": """    # 
    # 
    # 
#   # 
 ###  """,

"K": """#  # 
# #  
##   
# #  
#  # """,

"L": """#    
#    
#    
#    
#### """,

"M": """#   # 
## ## 
# # # 
#   # 
#   # """,

"N": """#   # 
##  # 
# # # 
#  ## 
#   # """,

"O": """ ###  
#   # 
#   # 
#   # 
 ###  """,

"P": """####  
#   # 
####  
#     
#     """,

"Q": """ ###  
#   # 
#   # 
#   # 
 ###  
    # """,

"R": """####  
#   # 
####  
# #   
#  ## """,

"S": """ ###  
#     
 ###  
    # 
 ###  """,

"T": """###### 
  ##   
  ##   
  ##   
  ##   """,

"U": """#   # 
#   # 
#   # 
#   # 
 ###  """,

"V": """#     # 
#     # 
 #   #  
  # #   
   #    """,

"W": """#     # 
#     # 
#  #  # 
 # # #  
  # #   """,

"X": """#   # 
 # #  
  #   
 # #  
#   # """,

"Y": """#   # 
 # #  
  #   
  #   
  #   """,

"Z": """##### 
   #  
  #   
 #    
##### """}
