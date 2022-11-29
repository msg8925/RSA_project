import rsa_algorithms
from decorators import login_required

###################################################
#  
#   Desc: Generate both the public and private keys
#
#   NUMBER_OF_BITS
#
###################################################
@login_required
def rsa_generate_key(NUMBER_OF_BITS):
    
    # Generate random prime numbers
    p = rsa_algorithms.generate_random_prime(NUMBER_OF_BITS)
    q = rsa_algorithms.generate_random_prime(NUMBER_OF_BITS)

    # Print prime values
    #print(f"p = {p}")
    #print(f"q = {q}")

    # Compute the product of p and q
    n = p * q

    #print(f"n = {n}")

    # Choose e such that gcd(e, phi_n) == 1.
    phi_n = (p - 1) * (q - 1)
    #print(f"phi_n = {phi_n}")

    
    # find e
    # Cycle through numbers for e which are less than the totient/phi
    e = 2
    while e < phi_n:
        # e must be co-prime to phi and
        # smaller than phi.
        if rsa_algorithms.gcd(e, phi_n) == 1:
            break
        else:
            e = e + 1
    

    # Print encryption value
    #print(f"e = {e}")

    # Choose d such that e * d % phi_n = 1.
    # Notice that we're using our modular_inverse from our work in the last chapter!
    d = rsa_algorithms.multiplcative_inverse(e, phi_n)
    #print(f"d = {d}")

    keys = [e, d, n] 

    #return ((p, q, d), (n, e))
    return keys



###################################################
#  
#   Desc: Encrypts data using the formula:
#         c = (msg ^ e) % n  
#
###################################################
def rsa_encrypt(msg, e, n):

    #print(f"Message data = {msg}")
 
    # Encryption c = (msg ^ e) % n
    c = pow(msg, e) 
    #print(f"c = pow({msg}, {e}) = {c}")
    
    c = c % n
    #print(f"Encrypted data = {c}")
 
    return c


###################################################
#  
#   Desc: Decrypts data using the formula:
#         m = (c ^ d) % n  
#
###################################################
def rsa_decrypt(c, d, n):

    m = pow(c, d)
    #print(f"m = pow({c}, {d}) = {m}")
    
    m = m % n
    #print(f"Original Message Sent = {m}")    

    return m