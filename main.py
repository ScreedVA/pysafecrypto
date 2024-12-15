from rsa import KeyGenerator


key_generator = KeyGenerator()

key = key_generator.generate()
print(key)


