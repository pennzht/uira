# de Bruijn Leap

import string

def sequence (alphabet, width):
    # From WP.

    k = len(alphabet)
    n = width

    a = [0] * k * n
    ans = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                ans.extend (a[1 : p+1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range (a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
        # print ('result', t, p, a, ans)

    db(1, 1)
    return ''.join (alphabet[i] for i in ans)

# keyboard alphabet
# kbd_alpha = 'fjdkslahgeiruwotyqpvmbncxz'
# keyboard alphabet, easily recognizable
kbd_alpha = 'fjdklhgirwotyncxzaseuvmqpb'
assert sorted (kbd_alpha) == sorted (string.ascii_lowercase)

def sized_sequence (size):
    'Generates a de Bruijn sequence portion with a given size, sufficient to fill up the screen.'
    k = len (kbd_alpha)
    for width in range (1, size+1):
        if k ** width >= size:
            final_width = width
            break
    for subset in range (1, k+1):
        if subset ** final_width >= size:
            final_subset = subset
            break

    return {
        'sequence': sequence (kbd_alpha[:final_subset], final_width) [:size],
        'width': final_width,
        'subset': kbd_alpha[:final_subset],
    }

def sized_sequence_3 (size):
    'Generates a de Bruijn sequence portion with a given size, sufficient to fill up the screen. Always 3-lettered.'
    k = len (kbd_alpha)
    final_width = 3
    for subset in range (1, k+1):
        if subset ** final_width >= size:
            final_subset = subset
            break

    return {
        'sequence': sequence (kbd_alpha[:final_subset], final_width) [:size],
        'width': final_width,
        'subset': kbd_alpha[:final_subset],
    }

def _sized_sequence_test ():
    print (sized_sequence (12))
    print (sized_sequence (20))
    print (sized_sequence (500))
    print (sized_sequence (33*80))
    print (sized_sequence (3333))

