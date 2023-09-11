#Calculate the sum of unique "hip numbers" within a certain range
def isHipNum(n):
    return ((n+1)**2 + n**2)

def sumOfN(n):
    hipNum = []
    i = 1
    while len(hipNum) < n:
        if isHipNum(i) not in hipNum:
            hipNum.append(isHipNum(i))
        i += 1
    return sum(hipNum)

n = 12345
print(sumOfN(n))

#Count the frequency of words within the given string
def wordFrequencies(string):
    words = string.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    product = 1
    for word, frequency in frequency.items():
        product *= frequency
    return product

string = "date date fig apricot blueberry cherry strawberry fig strawberry apple fig date cherry cherry cherry cherry blueberry cherry blueberry apple blueberry blueberry blueberry blueberry cherry date fig banana blueberry apricot blueberry apple date apple cherry grapefruit cherry cherry banana grapefruit strawberry date banana grapefruit strawberry banana fig cherry strawberry strawberry apple strawberry fig apple blueberry strawberry grapefruit fig blueberry blueberry grapefruit banana cherry apple strawberry strawberry apple cherry grapefruit banana date apricot fig date cherry banana cherry grapefruit grapefruit banana grapefruit apple date fig cherry banana blueberry apricot apricot blueberry cherry banana blueberry blueberry apricot apple fig strawberry apple cherry"
print(wordFrequencies(string))

#Find the sum of all the integers in the given file that are strictly greater than 75
def sumUp75(filename):
    with open(filename, 'r') as file:
        numbers = file.read().split()
    sum = 0
    for num in numbers:
        if int(num) > 75:
            sum += int(num)
    return sum

filename = "nums.txt"
print(sumUp75(filename))

# Given a string as input, output a new string where: A. Every occurence of the letter X has been replaced with a Y, and B. every vowel(A,E,I,O,U) has been moved to the end of the string, in the same order as in the original string.
def shiftString(string1):
    vowels = []
    newString = string1.replace('X', 'Y')
    for char in string1:
        if char in 'A E I O U a e i o u':
            vowels.append(char)
    return newString + ''.join(vowels)

string1 = "EXAMPLE"
print(shiftString(string1))