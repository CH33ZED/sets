#Ziyan Lin and Max Bertfield


def union(a, b):
    g = [ x for x in a if not(x in b)]
    g += b
    return g;


def intersection(a, b):
    g = [ x for x in a if x in b]
    return g;


def set(a,b):
      g = [x for x in a if not(x in b)]
      return g;


def sydiff(a,b):
	g = [x for x in a if not(x in b)]
	g += [x for x in b if not(x in a)]
	return g;

def cp(a, b):
	g = [[x,y] for y in b for x in a if not(x in b)]
	return g;
