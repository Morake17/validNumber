
class Charge:
    def __init__(self, q, x, y):
        self.q=q
        self.x=x
        self.y=y

    def potential_at(self, a, b):
        answer = 0
        #do calculation to caluculate potential...me i dont remember it

        return answer


q1 = Charge(1,5,7)

print(str(q1))

print(q1.potential_at(5,7))