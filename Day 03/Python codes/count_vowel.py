def cnt_vowels(st):
    vw = "aeiou"
    ct = 0

    for ch in st.lower():
        if ch in vw:
            ct += 1

    return ct


st = input("Enter a string: ")
print(cnt_vowels(st))