def all_variants(text):
    for size in range(len(text)):
        for start in range(len(text) - size):
            yield text[start:start + size + 1]

a = all_variants("abc")
for i in a:
    print(i)