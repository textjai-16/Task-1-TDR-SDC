# Problem Set 4A


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
##    perm = []
##    if len(sequence) == 1:
##        print(sequence)
##        perm.append(sequence)
##        print(perm)
##        return perm    
##    else:
##        print(sequence)
##        perm = get_permutations(sequence[1:])
##        print(perm)
##        
##        for i in perm:
##            for j in range(len(i) + 1):
##                if j == 0:
##                    new = sequence[0] + i[1:]
##                elif j == len(i):
##                    new = i[:len(i)] + sequence[0]
##                else:
##                    new = i[:j] + sequence[0] + i[j:len(i) + 1]
##                print(new)
##                perm.append(new)
##            for i in perm:
##                if len(i) < len(sequence):
##                    perm.remove(i)
##            
##                
##        return perm



    if len(sequence) == 1:
        return [sequence]

    perm = []
    for i in range(len(sequence)):
        for j in get_permutations(sequence[1:]):
            s = j[:i] + sequence[0] + j[i:]
            perm.append(s)
    return perm










if __name__ == '__main__':
    x = input('Enter word: ')
    print(get_permutations(x))

#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


