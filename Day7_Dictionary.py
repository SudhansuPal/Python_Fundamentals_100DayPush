Dictionary = {'Name': 'Pat', 'job': ['dev'], 'age': 40} #Using a list for job so that it can hold multiple items  
Dictionary['job'].append('mgr')     #append only works on lists
Dictionary['job'].append('janitor')  
print(Dictionary)
print()



#nested dictionary

team = {
    'member1': {
        'name': 'Pal',
        'role': 'Hero',
        'skills': ['Python', 'Git']
    },
    'member2': {
        'name': 'Bob',
        'role': 'Builder',
        'skills': ['Building', 'Bricks']
    }
}
print(team['member1']['role'])  
team['member1']['skills'].append('Docker')
team['member3'] = {'name': 'Charlie', 'role': 'Manager', 'skills': ['Leadership']}
team.pop('member2')
print(team.keys()) 
print(team.values())
print(team)


