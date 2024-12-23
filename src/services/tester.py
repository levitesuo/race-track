class d:
    def __init__(self):
        self._hull = []

    def stuff(self, p, c):
        i = self._hull.index(p)
        hull = self._hull[0:i+1] + [c] + self._hull[i+1:]
        self._hull = hull.copy()


j = d()
j._hull.append('a')
j._hull.append('c')
j._hull.append('e')

print(j._hull)
j.stuff('a', 'b')
print(j._hull)
j.stuff('c', 'd')
print(j._hull)
j.stuff('e', 'f')
print(j._hull)
