from rsa import KeyGenerator


key_gen = KeyGenerator(debug=True)

print(key_gen.generate())