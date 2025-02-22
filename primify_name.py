from alphabet import alphabet, concat_letters, expand, subs, to_word
from sympy.ntheory import nextprime, isprime


# ~ for letter in alphabet:
    # ~ lengths = [len(n) for n in alphabet[letter].split("\n")]
    # ~ if len(set( lengths )) != 1:
        # ~ print("NOT SAME SIZE!!!")
        # ~ raise SyntaxError(letter + ": " + str(lengths))

def to_int(string, factor = 3):
    letters = expand(to_word(string), factor)
    letters = subs(letters).replace("\n", "")
    return int(letters)

def primify(name, expansion_factor = 2):
    num = to_int(name, expansion_factor)
    num = nextprime(num)
    # uncomment the next line to find the next "sexy" prime.
    # while not isprime(num + 6): num = nextprime(num)
    lengths_of_lines = [len(line) for line in expand(to_word(name), expansion_factor).split("\n")]
    ans = ""
    strnum = str(num)
    for length in lengths_of_lines:
        ans += strnum[:length]
        ans += "\n"
        strnum = strnum[length:]
    return ans

def doublePrimify(name1, name2, shared_end="", expansion_factor = 2):
    num1 = to_int(name1, expansion_factor)


if __name__ == "__main__":
    has_went = False
    while (not has_went) or input("Another name? (Y/N): ").upper() == "Y":
        has_went = True    
        name = input("What is the name you would like to generate?\n>>> ").upper()
        expansion_factor = input("What is the expansion factor? (Leave blank for default)\n>>> ")
        print()

        if expansion_factor == "":
            expansion_factor = 3
        else:
            expansion_factor = int(expansion_factor)

        prime = primify(name, expansion_factor)
        print(prime)

        option = input("Would you like to save the name? (Y/N): ").upper()

        # save prime number to name.txt
        if option == "Y":
            file_out = open("name.txt", "a")
            file_out.write(prime)
            file_out.close()
            print("Name saved to name.txt")
