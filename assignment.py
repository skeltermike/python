def palindrome(m):
    return m == m[::-1]

m = "rotator"
ans = palindrome(m)

if ans:
    print("yes")
else:
    print("no")
