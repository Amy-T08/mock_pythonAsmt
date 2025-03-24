
score = 0 

Qa = {
    }

def main():
    score = 0
    for k,v in Qa.items():
        user_ans = input(f'What is the capital of {k}: ')
        if user_ans == v:
            print('correct')
            score+=1
        else:
            print('incorrect')

    print(score)

def details():
    name = input('Enter your name: ')
    if name == '':
        print("This field can't be blank")
    year_lvl = int(input('Enter your year level: '))
    
