
empty = []

def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            empty.append(i)

x = [[1,"a",["cat"],2],[[[3]],"dog"],4,5]
flatten(x)
print(empty)