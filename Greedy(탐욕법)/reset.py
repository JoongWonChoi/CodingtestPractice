print("This is git reset test")
print("changed in test branch")
def sum(a,b):
    return a+b

def testsum(a,b):
    return a+b

<<<<<<< HEAD
<<<<<<< Updated upstream
def pr_stash():
    print("should be in master branch")
    return
=======
def git_stash_pop():
    pop = apply + drop
    print("practice git stash pop")
>>>>>>> Stashed changes
=======
'''practice git stash pop'''

def non_cherry_picked():
    print("not in cherry-picked.")
    return

def cherry_picked():
    print("in cherry-picked.")
    return


>>>>>>> f81ca50 (Git -practice --Add cherry picked function)
