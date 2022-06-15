print('This is our main test file')

def field_size_inp():

    try:
        field_side = int(input('Field sice: '))
        return field_side
    except:
        field_side = 'wrong_input'
        return field_side


while True:
    field_side = field_size_inp()
    if field_side == 'wrong_input':
        print('Please enter a valid number')
    else:
        field_size = field_side * field_side
        snake_len = 1
        feeding = 0
        while snake_len < field_size:
            snake_len = snake_len * 2
            if snake_len <= field_size:
                feeding += 1
            else: continue
        print(feeding)


#comment -  this is a test comment

