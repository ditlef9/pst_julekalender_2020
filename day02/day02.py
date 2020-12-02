class Day02:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 02 ~~~~~~~~~~~~~~~~~~~~~~~~')
    string = repr(open("./day02/pen_gwyn_greatest_hits.mid", 'rb').read())
    string_solution=""
    start_position = 194
    interval = 22
    i = 0
    char_number = 0

    for char in string:
        char_number+=1
        i+=1
        if char_number > start_position:
            if i>=interval:
                string_solution=string_solution+char
                i=0
    print(string[start_position:])
    print(string_solution)