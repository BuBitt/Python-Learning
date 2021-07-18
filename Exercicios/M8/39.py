a = 7777777777777
b = 8888888888888

print(f"""Before:
{a} <- A
{b} <- B""")


def troca(x, y):
    temp = []
    temp.append(x)
    temp.append(y)
    x = temp[1]
    y = temp[0]
    print(temp, x, y)


troca(a, b)

print(f"""\nAfter:
{a} <- A
{b} <- B""")
