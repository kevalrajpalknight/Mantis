function hello -- x, y, z (
    return x + y + z
)

loop i -- range(37) (
    output(hello(loop.step, 1, 2))
)

output(location.line)
# COMMENT

/*
Multi
Line
Comment
*/


loop char from "qwertyuiopasdfghjklzxcvbnm" (
    output(loop.step)
    if loop.step == 'n':
        output(f'On letter <loop.step>')
    else:
        pass
)

number = 0 + 1 + 2 / 3 * 8

list_of_nums = [1, 2, 3, 4, 5, 6]
# Here we will multiply all the values in list_of_nums

output(list_of_nums)

# Here we will use input() to, well, get an input
output(input('Say something:'))
