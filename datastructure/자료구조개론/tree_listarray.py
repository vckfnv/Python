Tree=[0]
def search(p,Tree,data):
    if Tree[p] == 0:

    if Tree[p] == data:

    if Tree[p] < data:
        search(2*p+1,Tree,data)

    if Tree[p] > data:
        search(2*p,Tree,data)
