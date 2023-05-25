from collections import namedtuple

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.readlines()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = [] #Complete this - medals is a list of medal namedtuples
for line in olympics[1:]:
    values = line.strip().split(";")
    medals.append(medal(*values))


def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    def found(args:list, fline: namedtuple):
        for arg in args:
            #print("arg",arg,getattr(fline ,arg[0],None))
            if getattr(fline ,arg,None) != args[arg]:
                return False
        return True
    

    #first.items() <= second.items() is first subset of second
    return list(filter(lambda x: found(kwargs,x),medals))

#print(get_medals(Edition="1896"))
actual = get_medals(Athlete='LEWIS, Carl', Event='100m')
print(actual)
expected = [medal(City='Los Angeles', Edition='1984', Sport='Athletics', Discipline='Athletics', Athlete='LEWIS, Carl', NOC='USA', Gender='Men', Event='100m', Event_gender='M', Medal='Gold'),
            medal(City='Seoul', Edition='1988', Sport='Athletics', Discipline='Athletics', Athlete='LEWIS, Carl', NOC='USA', Gender='Men', Event='100m', Event_gender='M', Medal='Gold')]
print(expected)