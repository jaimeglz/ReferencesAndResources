# Compute the decimals of Pi using the Wallis formula:

def piWallis(numIter=100000):
    """ Computes pi in accordante to Wallis' formula.
    Use:
        piWallis(numIter)
        Where: numIter is the number of iterations to be performed.
        If numIter is left unspecificied, iterates 100,000 times
        
        Please keep in mind that Wallis' formula converges to pi rather slowly.
        1,000,000 iterations would give a more accurate value.
    """
    ans = 1
    for i in range (1,numIter+1):
        ans = (   ( 4.0*(i**2 ) ) / (  ( 4.0 * (i**2) - 1)  )   ) * ans

    return 2 * ans