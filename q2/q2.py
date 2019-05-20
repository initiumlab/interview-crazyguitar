def changeStyle(string):
    return ''.join([s.title() for s in string.split('_')])

for i in ['under_score' , 'open_door', 'sort_by_id']:
    print(changeStyle(i))
