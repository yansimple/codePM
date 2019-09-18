# by YANSIMPLE
def prettyPATH(x):
    items = x.split("/")
    
    path_items = list(items[1:])

    for i in path_items:
        if i == "..":
            index = path_items.index(i)
            path_items.pop(index-1)
            path_items.pop(index-1)

    for i in path_items:
        if i == ".":
            index = path_items.index(i)
            path_items.pop(index)

    string = "/".join(path_items)
    string = '/'+string

    return string