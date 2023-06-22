import random

def western_names():
    first_names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Elijah', 'Charlotte', 'William', 'Sophia',
                   'James', 'Amelia', 'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Harper', 'Alexander', 'Evelyn',
                   'Sebastian', 'Abigail', 'Jack', 'Emily', 'Samuel', 'Elizabeth', 'Daniel', 'Mila', 'Matthew', 'Ella',
                   'David', 'Scarlett', 'Joseph', 'Grace', 'Carter', 'Chloe', 'Owen', 'Victoria', 'Wyatt', 'Madison',
                   'John', 'Luna', 'Michael', 'Zoe', 'Ethan', 'Penelope', 'Anthony', 'Lily', 'Daniel', 'Sofia']
    
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Miller', 'Wilson', 'Anderson', 'Thomas', 'Jackson', 'White',
                  'Harris', 'Martin', 'Lewis', 'Clark', 'Walker', 'Hall', 'Young', 'King', 'Wright', 'Adams', 'Baker',
                  'Green', 'Carter', 'James', 'Lee', 'Turner', 'Parker', 'Collins', 'Morris', 'Hughes', 'Reed', 'Cook',
                  'Murphy', 'Bennett', 'Watson', 'Wood', 'Cooper', 'Reynolds', 'Gonzalez', 'Hill', 'Nelson', 'Mitchell',
                  'Roberts', 'Campbell', 'Perez', 'Gray', 'Rogers', 'Stewart', 'Sanchez', 'Scott', 'Ramirez']
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return first_name + " " + last_name

def chinese_names():
    characters = ['Wei', 'Wu', 'Xi', 'Ming', 'Lu', 'Lang', 'Chao', 'Shao',
                  'Yi', 'Jin', "Qi", "Qing", "Qi", "Da", "Tai", "Wan",
                  "Bei", "Jing", "Li", "Wang", "Yang", "Xu", "Xiao",
                  "Dong", "Zhou", "Mao", "Ze", "Deng", "Ping"]
    chinese_name = random.choice(characters) + " " + random.choice(characters) + random.choice(characters)
    return chinese_name


# Example usage
#for _ in range(50):
#    print(chinese_names())
#    print(western_names())
