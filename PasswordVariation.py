from itertools import product
commonSubs = {
"a": ["@","4"],
"b": ["8"],
"e": ["3"],
"g": ["6","9"],
"i": ["1","!"],
"o": ["0"],
"s": ["5","$"],
"t": ["7","+"],
}

# This code generates variations of a given password by applying different capitalization 
# and common substitutions to each character in the password.
def genVariations(password):
    variations = [""]
    for p in password:
        uppers = [v+p.upper() for v in variations]
        lowers = [v+p.lower() for v in variations]
        vs = uppers + lowers
        if p in commonSubs:
            for s in commonSubs[p]:
                x = [v+s for v in variations]
                vs += x
        variations = vs
    return variations

#This code generates suffixes by combining special characters and numbers in different combinations.
special = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
def genSuffixes():
    specs = [x for x in special]
    nums = [str(n) for n in range(100)]
    combos = list(product(specs,nums))
    sn = [c[0]+c[1] for c in combos]
    ns = [c[1]+c[0] for c in combos]
    return sn+ns

# This code generates passwords by combining variations of a given password with suffixes.
def genPasswords(password):
    variations = genVariations(password)
    suffixes = genSuffixes()
    passwords = variations+[[v+s for v in variations] for s in suffixes]
    return passwords
