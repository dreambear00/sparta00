fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
def CountFruit(FruitName):
    count = 0
    for i in fruits:
        if i == FruitName:
            count += 1
    print(count)



    people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]


for person in people:
    print(person['name'], person['age'])

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'


    print(get)
