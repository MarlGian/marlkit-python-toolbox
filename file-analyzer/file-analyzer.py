import sys

def word_count(files):
    with open(files, "r") as file:
        word_count = file.read().replace(",", " ").split()

    return(f"{len(word_count)} total words in {files}")
    
    
def letter_count(file):
    with open(file, "r") as f:
        letter_counts = f.read()
        letters = [char for char in letter_counts if char.isalpha()]
        
    return(f"{len(letters)} total letters in {file}")
    
  
def number_count(file):
    with open(file, "r") as f:
        num_read = f.read()
        num = [char for char in num_read if char.isdigit()]
        
    return(f"{len(num)} total numbers in {file}")

def word_frequency(file):
    unique = {}

    with open(file, "r") as f:
        text = f.read().lower().replace(",", " ")
        words = text.split()

    for word in words:
        if word in unique:
            unique[word] += 1
        else:
            unique[word] = 1

    result = ""
    for key, value in sorted(unique.items()):
        result += f"{key} : {value}\n"    
    return result

txtfile = sys.argv[1]
    

if len(sys.argv) < 3:
    print("Usage: python file-analyzer.py <filename> <flag>")
    print("Flags: --count-let, --count-word, --count-num, --word-freq")
    sys.exit()

arg3 = sys.argv[2]

if arg3 == "--count-let:":
    print(letter_count(txtfile))
elif arg3 == "--count-word":
    print(word_count(txtfile))
elif arg3 == "--count-num":
    print(number_count(txtfile))
elif arg3 == "--word-freq":
    print(word_frequency(txtfile))
else:
     print("Flags: --count-let, --count-word, --count-num, --word-freq")
