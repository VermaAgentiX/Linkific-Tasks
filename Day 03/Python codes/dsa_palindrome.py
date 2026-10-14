def is_palindrome(st):
    st = st.lower()
    return st == st[::-1]


st = input("Enter a string: ")

if is_palindrome(st):
    print("Palindrome")
else:
    print("Not a palindrome")