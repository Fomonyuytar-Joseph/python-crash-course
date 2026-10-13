# Complete the solution so that it reverses the string passed into it.

# 'world' = >  'dlrow'
# 'word'   = >  'drow'

def solution(string):
    rev = ""
    for i in range(len(string) - 1, -1,-1):
        rev+=string[i]
    return rev

    # return string[::-1]

print(solution('world'))
