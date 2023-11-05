a=int(input('Enter the value: '))
match a:
    case 0:
        print('You are beautiful !')
    case 4:
        print('You are ugly')
    case _ if a !=90:
        print('not equal to 90 !')
    case _ if a !=80:
        print('not equal to 80')
  
    case _:
        print('you are wrong')



