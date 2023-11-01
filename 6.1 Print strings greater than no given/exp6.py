def string_k(k, st):
    string=[]
    text=st.split(" ")

    for x in text:
        if len(x)>k:
            string.append(x)

    return string

k=int(input("Enter a no to check greater than of:"))
st=str(input("Enter a string"))
print(string_k(k, st))
