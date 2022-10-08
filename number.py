import math

class Number:
    def __init__(self,n):
        self.n=n

    def data_type(self):
        """Find the datatype of given value
        Returns:
            _type_: Type of given value
        """
        return type(self.n)

    def len_value(self):
        """Find the len of given value
        Returns:
            int: len of the value
        """
        return len(str(self.n))

    def is_positive(self):
        """Determine given value is positive number
        Returns:
            bool: True if positive number
        """
        return self.n>0
    
    def is_negative(self):
        """Determine given value is positive number
        Returns:
            bool: True if negative number
        """
        return self.n<0
    
    def is_zero(self):
        """Determine given value is equals zero
        Returns:
            bool: True if the value is equal 0
        """
        return self.n==0

    def is_even(self):
        """Determine given value is even number
        Returns:
            bool: True if the value is equal even number
        """
        return self.n%2==0

    def is_odd(self):
        """Determine given value is odd number
        Returns:
            bool: True if the value is equal odd number
        """
        return self.n%2!=0

    def is_prime(self):
        """Determine given value is prime number
        Returns:
            bool: True if the value is include prime number
        """
        prime_nums = []
        if self.n>1:
            for i in range(1,self.n+1):
                if self.n%i==0:
                    prime_nums.append(i)
            return len(prime_nums)==2
        else:
            return None
    def int_str(self):
        """Determine given value is str or int
        Returns:
            str: str if given value is int else pass
        """
        if type(self.n)==str:
            pass
        else:
            return str(self.n)

n1 = Number(2)
print(n1.is_prime())