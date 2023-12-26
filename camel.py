def main():
    name = input('Верблюжий стиль: ')
    convert(name)

def convert(camel):
    for c in camel:
        if c.isupper():
            c = c.lower()
            print('_', c, sep='', end = '')
        else:
            print(c, end = '')
    print()

main()