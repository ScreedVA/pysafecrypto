import random


class PrimeHandler:
    def __init__(self, prime_range_start: int=100, prime_range_end: int=250) -> None:
        """Initialize configuration for primehandler"""
        self.pr_start = prime_range_start
        self.pr_end = prime_range_end

    def gen_prime_fact(self) -> int:
        """Generates a prime number within the initalized pr ranges"""
        p: int
        while True:
            p = random.randrange(self.pr_start, self.pr_end) # Choose random integer within given range
            if self.is_prime(p): # Check if integer is prime
                return p


    def eval_gcd(self, a: int, b: int, chained:bool=False) -> int | dict:
        """Implements Euclidean algorithm to find gcd between a and b

        -- Will return dictionary of chained equation sequence if chained parameter is set to True otherwise
        will simply return gcd
        """
        # Input Validation
        if not self._is_integer(a):
            raise ValueError(f"a:'{a}' is not an integer.")
        
        elif not self._is_integer(b):
            raise ValueError(f"b:'{b}' is not an integer.")
        elif not isinstance(chained, bool):
            raise ValueError(f"chained:'{chained}' is not a bool")
        # Ensure a and b are operable
        a = int(a)
        b = int(b)

        if a <= b:
            raise ValueError(f"a:'{a}' must be greater than b:'{b}'")
        if int(a) <= 1:
            raise ValueError(f"a:'{a}' must be greater than 1")
        
        q: int
        r: int
        gcd: int = -1
        q = a // b # Find the quotient as an integer
        r = a % b # Find the remainder as an integer

        # Initialize chain
        
        chain: dict[list] = {
            "chain": [{"id": 0, "a": a, "b": b, "q": q, "r": r}]
        } 

        # Divide previous remainder(r) into previous divisor(b) 
        while r != 0:
            if b % r == 0:
                gcd = r
            a = b # Reset dividend
            b = r # Reset divisor
            q = a // b
            r = a % b
            if chained:
                id = len(chain["chain"])
                chain["chain"].append({"id": id, "a": a, "b": b, "q": q, "r": r})
        chain["gcd"] = gcd
        if chained:
            return chain
        return gcd


    def gen_coprime(self, n: int) -> int:
        """Finds coprime for given integer(n)"""
        if not self._is_integer(n):
            raise ValueError(f"n:'{n}' is not an integer.")

        e: int
        while True:
            e = random.randrange(2, n)
            if self.eval_coprime(a=n, b=e):
                return e


    def eval_mult_inv(self, e: int, n: int):
        """Brute force implementation to find multiplicative inverse modulo(d) given the integer 'e' and modulo 'n' """
        # Check if multiplicative inverse exists
        if not self.eval_coprime(n, e):
            return None
        
        # Stops once iterations reach the range of integer(e)
        for d in range(n - 1): 
            if (e * d) % n == 1:
                return d


    def eval_coprime(self, a: int, b: int):
        """Checks if integer(a) is coprime with integer(b)"""
        if self.eval_gcd(a, b) == 1:
            return True
        return False



    def is_prime(self, a: int) -> True | False:
        """Checks if given input 'a' is a prime number"""
        if a <= 1:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True
    
    def _is_integer(self, value):
        """Returns true if input value is a digt otherwise ValueError"""
        try:
            int(value)
            return True
        except ValueError:
            return False

    def eval_diphon(self, a, b):
        """Implements back-substituiton to finds the diphontine equation corresponding to gcd(a,b)"""
        pass


if __name__ == "__main__":
    p_h = PrimeHandler()
    # print(p_h.gen_prime_fact())
    # print(p_h.eval_gcd(5000, 4059, chained=True))
    # print(p_h.eval_mult_inv(e=4059, n=5000))
    # print(p_h.gen_coprime(5000))
    print(p_h.eval_coprime(a=650560, b=509493))



# TODO Create a method to workout the diphontine equation of a given 


# -- DONE -- #

# TODO Create a class to handle prime factor generation

# -- DONE -- #

