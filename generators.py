def all_variants(text):
    for i in range(1, len(text) + 1):
        for start in range(len(text) - i + 1):
            yield text[start:start + i]

a = all_variants("abc")
for i in a:
    print(i)