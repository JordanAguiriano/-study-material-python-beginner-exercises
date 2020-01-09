def fizz_buzz():
    for fizzbuzz in range(1,101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
        elif fizzbuzz % 3 == 0:
            print("fizz")
        elif fizzbuzz % 5 == 0:
            print("buzz")
        else:
            print(fizzbuzz)


fizz_buzz()

# you have to write the first if statement 'if fizzbuzz % 3 == 0 
# and fizzbuzz % 5 == 0:' because if you put it last the code wont
# work. Colby says "a computer wont understand english sentence saying 
# 'everyone in the room take your tables out of the room unless you are 
# sitting at the table.'' instead a computer would say 'if you are sitting 
# on a table keep it in the room. if you are not sitting at the table take 
# that table out of the room.'"