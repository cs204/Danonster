def main():
    fruit = input('Фрукт: Калории: ')
    fruitlist = fruit.split(' ')
    fruitname = []
    for i in range(len(fruitlist)):
        fruitname.insert(-1, fruitlist[i - 1].lower().capitalize())

    fruit = ' '.join(fruitname)
    calories(fruit)


def calories(fruit):
    fruits = {
        'Apple' : 130,
        'Avocado' : 50,
        'Banana' : 110,
        'Cantaloupe' : 50,
        'Grapefruit' : 60,
        'Grapes' : 90,
        'Honeydew Melon' : 50,
        'Kiwifruit' : 90,
        'Lemon' : 15,
        'Lime' : 20,
        'Nectarine' : 60,
        'Orange' : 80,
        'Peach' : 60,
        'Pear' : 100,
        'Pineapple' : 50,
        'Plums' : 70,
        'Strawberries' : 50,
        'Sweet Cherries' : 100,
        'Tangerine' : 50,
        'Watermelon' : 80
    }

    if fruit in fruits:
        print(fruits[fruit])

main()