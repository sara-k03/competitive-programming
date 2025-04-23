initial_length = int(input())
initial_line = []

for i in range(initial_length):
    initial_line.append(input())

num_commands = int(input())
for i in range(num_commands):
    command_line = input()
    commands = command_line.split(' ')
    if ( commands[ 0 ] == "cut" ):
        index = initial_line.index( commands[ 2 ] ) 
        initial_line.insert( index, commands[ 1 ] )
    elif ( commands[ 0 ] == "leave" ):
        initial_line.remove( commands[ 1 ] )

for i in initial_line:
    print(i)

