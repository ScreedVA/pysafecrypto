from rsa.utility import PrimeHandler

class KeyGenerator(PrimeHandler):
    def __init__(self, debug=False) -> None:
        self.debug = debug
        super().__init__()


    def generate(self, debug=False):
        """Generates both public and private keys"""
        payload = self.__gen_private_key()
        if debug == True:
            self.debug = True
        else:
            self.debug = False

        return {
            "public key": (payload["e"], payload["n"]),
            "private key": (payload["d"], payload["n"])
        }


    
    
    def __gen_private_key(self):
        """Generates private key multiplicative inverse(d) given public key (e) and totient(tn)"""
        payload = self.__gen_public_key()
        n, tn, e = payload["n"], payload["tn"], payload["e"]
        d = self.eval_mult_inv(e=e, n=tn)
        return {"n": n, "tn": tn, "e": e, "d": d}


    def __gen_public_key(self):
        """Generate public key(e) given the totient (tn)"""
        n, tn = self.__gen_n_tn()
        e = self.gen_coprime(tn)
        return {"n": n, "tn": tn, "e": e}


    def __gen_n_tn(self) -> tuple[int, int]:
        """Returns semi-prime number(n), the product of two prime numbers (p) and (q) and (tn),
        the product of (p-1)(q-1)"""
        pq = self.__gen_pq()
        n: int = (pq[0] * pq[1])
        tn: int = ((pq[0] - 1) * (pq[1] - 1))

        if self.debug:
            print("\n------- OUTPUT AFTER __gen_n_tn() -------\n")
            print({"p": pq[0], "q": pq[1], "n": n, "tn": tn})
            print("\n------- OUTPUT AFTER __gen_n_tn() -------\n")
        return (n, tn)


    def __gen_pq(self) -> tuple[int,int]:
        """Generates 2 unique prime numbers (p) and (q)"""
        p: int = self.gen_prime_fact()
        q: int = self.gen_prime_fact()

        while p == q:
            q = self.gen_prime_fact()
        return (p,q)

