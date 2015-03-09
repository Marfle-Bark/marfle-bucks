__author__ = 'Ethan Busbee'

class Currency(object):
    def __init__(self, amount=None):
        self._uDollars = 0 # Number of micro-USD (for precision)
        if type(amount) is type(self):
            self._uDollars = amount.getExactAmount()
        elif amount is not None:
            self._uDollars = int(round(amount * 1000000))

    def getExactAmount(self): return self._uDollars
    def getApproxAmount(self): return float("{:1,.2f}".format(self._uDollars / 1000000.0)) # This is a dirty hack
    def toString(self): return "$" + "{:1,.2f}".format(self._uDollars / 1000000.0)

    def getDollarPart(self): return self._uDollars / 1000000
    def getCentPart(self): return (self._uDollars / 10000) % 100

    def add(self, other):
        if type(other) is not type(self):
            other = Currency(other)
        self._uDollars += other.getExactAmount()

    def sub(self, other):
        if type(other) is not type(self):
            other = Currency(other)
        self._uDollars -= other.getExactAmount()

    def mul(self, factor):
        self._uDollars *= factor
        self._uDollars = int(round(self._uDollars))

    def div(self, factor):
        self._uDollars /= factor
        self._uDollars = int(round(self._uDollars))

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
    print "It doesn't yet do conversion of any kind, so you'll need to write your own glue code."
    print "ALSO COMPARISONS ARE APPROXIMATE"
    print "Made with <3 by Ethan Busbee for his own learning."
    print ""

    print "***Init to $12.34"
    dough = Currency(12.34)
    print dough.toString()

    print "***Add $10"
    dough.add(10)
    print dough.toString()

    print "***Remove $5.00"
    dough.sub(5.00)
    print dough.toString()

    print "***Multiply by 5x"
    dough.mul(5)
    print dough.toString()

    print "***Divide by 5x"
    dough.div(5)
    print dough.toString()

    print "***Show dollars and cents separately."
    print "Dollars: " + str(dough.getDollarPart())
    print "Cents: " + str(dough.getCentPart())

    # Comparison Operators
    cash = Currency(10)
    money = Currency()
    money.add(5.50)
    money.add(5)
    money.sub(0.50)
    # cash and money should both be $10.00 at this point

    print "***Compare $10.00 == $10.00 and $10.00 != $10.01:"
    print cash == money
    print cash != money

    print "***Compare $10.00 == $10.01 and $10.00 != $10.01:"
    money.add(0.01) # make money be slightly higher than cash
    print cash == money
    print cash != money

    print "***Compare $10.01 < $10.00:"
    print money < cash

    print "***Compare $10.00 < $10.00:"
    print cash < money

    money.sub(0.01)
    print "***Compare $10.00 <= $10.00:"
    print cash <= money

    print "***Compare $10.00 >= $10.00"
    print cash >= money