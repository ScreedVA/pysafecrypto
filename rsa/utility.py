import random
# TODO Create a class to handle prime factor generation


class PrimeHandler:
    def __init__(self, prime_range_start: int=1000, prime_range_end: int=5000) -> None:
        """Initialize configuration for primehandler"""
        self.pr_start = prime_range_start
        self.pr_end = prime_range_end

    def generate_prime_factor(self) -> int:
        """Generates a prime number within the initalized pr ranges"""
        while True:
            p = random.randrange(self.pr_start, self.pr_end) # Choose random integer within given range
            if self.is_prime(p): # Check if integer is prime
                return p


    def eval_gcd(self, a: int, b: int, chained:bool=False) -> int:
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
        gcd: int
        q = a // b # Find the quotient as an integer
        r = a % b # Find the remainder as an integer

        # Initialize chain
        if chained == True:
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






    def eval_coprime(self, a, b):
        pass


    def eval_multiplicative_inverse(self, a, b):
        pass


    def is_prime(self, a: int) -> True | False:
        """Checks if given input 'a' is a prime number"""
        if a <= 1:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True
    

    def _is_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    p_h = PrimeHandler()
    # print(p_h.generate_prime_factor())
    print(p_h.eval_gcd(34, 14, chained=True))


