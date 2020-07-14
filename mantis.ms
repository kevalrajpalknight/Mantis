import some_package

function hello -- x, y, z (
    return x + y + z
)

loop i -- range(37) (
    output(hello(loop.step, 1, 2))
)

output(location.line)
// COMMENT

// COMMENT //

///
COMENT
///

loop char from "qwertyuiopasdfghjklzxcvbnm" (
    output(loop.step)
    if loop.step == 'n':
        output(f'On letter <loop.step>')
)

number = 0 + 1 + 2 / 3 * 8

list_of_nums = [1, 2, 3, 4, 5, 6]

output(list_of_nums)
