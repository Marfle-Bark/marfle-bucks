__author__ = 'Ethan Busbee'

class Currency(object):
    def __init__(self, amount=None):
        self._uDollars = 0 # Number of micro-USD (for precision)
        if type(amount) is type(self):
            self._uDollars = amount.getExactAmount()
        elif amount is not None:
            self._uDollars = int(round(amount * 1000000))

    def getExactAmount(self): return self._uDollars
    def getApproxAmount(self): return round(self._uDollars / 1000000.0, 2)
    def __str__(self): return "$" + "{:1,.2f}".format(self.getApproxAmount())

    def getDollarPart(self): return self._uDollars / 1000000
    def getCentPart(self): return (self._uDollars / 10000) % 100

    def __add__(self, other):
        if type(other) is not type(self):
            other = Currency(other)
        return Currency(self.getApproxAmount() + other.getApproxAmount())

    def __sub__(self, other):
        if type(other) is not type(self):
            other = Currency(other)
        return Currency(self.getApproxAmount() - other.getApproxAmount())

    def __mul__(self, factor):
        self._uDollars *= factor
        return Currency(self.getApproxAmount())

    def __div__(self, factor):
        self._uDollars /= factor
        return Currency(self.getApproxAmount())

    # Comparisons are defined as approximate: it only checks down to $0.01, NOT micro-dollars!
    def __lt__(self, other): return type(self) == type(other) and self.getApproxAmount() < other.getApproxAmount()
    def __le__(self, other): return self < other or self == other
    def __eq__(self, other): return type(self) == type(other) and self.getApproxAmount() == other.getApproxAmount()
    def __ne__(self, other): return not self == other
    def __gt__(self, other): return type(self) == type(other) and self.getApproxAmount() > other.getApproxAmount()
    def __ge__(self, other): return self > other or self == other



if __name__ == "__main__":
    print "Note: this class simulates down to micro-dollars to reduce rounding error."
    print "Also, right now this class ONLY handles USD and all output is formatted with regards to that."
    print "It doesn't yet do currency conversion of any kind, so you'll need to write your own glue code."
    print "ALSO COMPARISONS ARE APPROXIMATE TO ONE PENNY"
    print "Made with <3 by Ethan Busbee for his own learning."
    print ""

    dough = Currency(12.34)
    print "***Init to $12.34: " + str(dough)

    dough += 10
    print "***Add $10: " + str(dough)

    dough -= 5.00
    print "***Subtract $5.00: " + str(dough)

    dough *= 5
    print "***Multiply by 5x: " + str(dough)

    dough /= 5
    print "***Divide by 5x: " + str(dough)

    print "***Show dollars and cents separately:"
    print "***Dollars: " + str(dough.getDollarPart()) + ", Cents: " + str(dough.getCentPart())

    # Comparison Operators
    cash = Currency(10)
    money = Currency(10.00)
    # cash and money should both be $10.00 at this point
    print "***Compare $10.00 == $10.00: " + str(cash == money)
    print "***Compare $10.00 != $10.00: " + str(cash != money)

    money += 0.01 # make money be slightly higher than cash
    print "***Compare $10.00 == $10.01: " + str(cash == money)
    print "***Compare $10.00 != $10.01: " + str(cash != money)

    print "***Compare $10.01 < $10.00: " + str(money < cash)
    print "***Compare $10.00 < $10.01: " + str(cash < money)

    money -= 0.01
    print "***Compare $10.00 < $10.00: " + str(cash < money)
    print "***Compare $10.00 <= $10.00: " + str(cash <= money)
    print "***Compare $10.00 >= $10.00: " + str(cash >= money)