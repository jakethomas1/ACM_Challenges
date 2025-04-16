rm_dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 } #convert letter to number

def convertRomanNumeral(str1):
    total = rm_dict[str1[-1]]
    for char in reversed(str1[:-1]):
        
        if(rm_dict[char] < total-1): #e.g. for III; 3rd loop: rm_dict[char]=1, total-1=1... eval to False 
            total -= rm_dict[char]
        else:
            total += rm_dict[char]
        
    return total


        #e.g. XLIX: start at end X=10 add to total; I=1 ->  1 < total -> total - I; L=50, L > total(9), L + total; X=10, X < total, total - X; 
        #e.g. LIII: I=1 add to total; I=1 I==total; I+1 
        #if(rm_dict[char] <= total -1): 





examples = ["IV", "IX", "XLIX", "LIII", "LX", "XCIX", "CCXXXIV", "MCCCLXIII", "MCDLXIV"] #4, 9, 49, 53, 60, 99, 234, 1363, 1464

for example in examples:
    print(example, convertRomanNumeral(example))