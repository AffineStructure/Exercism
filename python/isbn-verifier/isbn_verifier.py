from functools import reduce
def verify(isbn):
    isbn = isbn.replace("-","")
    try:
        isbn = [int(i) for i in isbn]
    except:
        return "not valid isbn"
    multi = list(reversed(range(1,11)))
    output = [isbn[i] * multi[i] for i in range(len(isbn))]
    return (reduce(lambda x,y: x+y, output) % 11 == 0)