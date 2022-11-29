from Crypto.Util import number

###################################################
#  
#   Desc: Find the greatest common divisor 
#         (Highest common factor) of 'A' and 'B' 
#         using Euclid's algorithm 
#          
###################################################
def gcd(A, B):

    r=0  
    a=0
    b=0

    if A > B: 
        a = A
        b = B
    else:
        a = B
        b = A
        

    # Euclid's algorithm (Find GCF/HCF of two numbers 'A' and 'B')
    while 1:
        
        # Show iterations of GCD algorithm
        # printf("a: %d, b: %d, r: %d\n", a, b, r);    

        if b == 0:
            return a
        
        
        r = a % b    

        # Shift B into A and R into B for the next iteration  
        a = b
        b = r   


###################################################
#  
#   Desc: Finds the multiplicative inverse using the
#         extended Euclid's algorithm    
#
###################################################
def multiplcative_inverse(A, B):

    a=0
    b=0
    r=0
    T=0
    T1=0
    T2=1
    Q=0

    # Ensure that a's value is always larger than a's value
    if A > B:
        a = A
        b = B
    
    else:
        a = B
        b = A
        

    # Euclid's algorithm (Find GCF/HCF of two numbers 'A' and 'B')
    while 1:
        
        # Show iterations of EEA algorithm
        #print(f"Q: {Q}, a: {a}, b: {b}, r: {r}, T1: {T1}, T2: {T2}, T: {T}", Q, a, b, r, T1, T2, T)    

        if b == 0:
            if T1 < 0:
                T1 = T1 + T2
            
            #print(f"T1={T1}")
            return T1
        

        # r = a mod b
        # a % b;
        r = a % b
        Q = a // b

        # T = T1 - (T2 * Q) 
        T = T1 - (T2 * Q)

        # Shift B into A and R into B for the next iteration  
        a = b
        b = r   

        # Shift T2 into T1 and shift T into T2
        T1 = T2
        T2 = T  


###################################################
#  
#   Desc: Generates a random prime with a bit size  
#         given by the argument 'NUMBER_OF_BITS'
#
###################################################    
def generate_random_prime(NUMBER_OF_BITS):

    # Use the 'Crypto' library to generate a random prime number
    return number.getPrime(NUMBER_OF_BITS)

  