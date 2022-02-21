"""
первая программа на Пайтон
"""
# print("Hello World")
#
# text = input("Please, enter your text here: ")
text = "Einstein excelled at math and physics from a young age, reaching a mathematical level years ahead of his peers."\
    "The 12 years old Einstein taught himself algebra and Euclidean geometry over a single summer. Einstein also "\
    "independently discovered his own original proof of the Pythagorean theorem at age 12. A family tutor Max Talmud "\
    "says that after he had given the 12 years old Einstein a geometry textbook, after a short time Einstein had" \
    "worked "\
    "through the whole book. He thereupon devoted himself to higher mathematics. Soon the flight of his mathematical "\
    "genius was so high I could not follow. His passion for geometry and algebra led the 12 years old to become "\
    "convinced that nature could be understood as a mathematical structure. Einstein started teaching himself calculus"\
    "at 12, and as a 14 years old he says he had mastered integral and differential calculus."
text = text.lower()

symbol_list = list(text.strip(''))
for i in symbol_list:
    if i == '.' or i == ',' or i == '?' or i == '!' or i == ':' or i ==';':
        symbol_list.remove(i)
text = ''.join(symbol_list)

word_list = text.split(" ")
word_set = set(word_list)

occurences = {}

for i in word_set:
    occurences[i] = ''

for i in occurences:
    occurences[i] = word_list.count(i)
print(occurences)
