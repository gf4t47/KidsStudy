from word_dictionary import shapes, colors
from randomization import shuffle_list
from format import markdown

s = shuffle_list(shapes)
f = markdown(s)

print(s)

c = shuffle_list(colors)
print(c)
