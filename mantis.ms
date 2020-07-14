import some_package

function hello -- x, y, z (
    stuff = x + y + z
    return stuff
)

# output() is the same as print()
loop -- int: 37, step: 1 (
    output(hello(loop.step, 1, 2))
)

output(location.line)

///
Here we are looping
through a string of
characters. Cool!
///

loop -- char: "qwertyuiopasdfghjklzxcvbnm" (
    output(loop.step)
    if loop.step == 'n':
        output(f'On letter [loop.step]')
)

number = 0

function number.on_update -- number.new_val, number.past_val (
    output('Number was', number.past_val, 'but is now', number.new_val)
)
number = 10

list_of_nums = [1, 2, 3, 4, 5, 6]
2*all in list_of_nums.all
# list_of_nums is now equal to [2, 4, 6, 8, 10, 12]

output(list_of_nums)
