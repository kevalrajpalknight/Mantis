import some_package

function hello -- x, y, z (
    stuff = x + y + z
    return stuff
)

loop int: 37 (
    output(hello(loop.step, 1, 2))
)

output(location.line)

loop char: "qwertyuiopasdfghjklzxcvbnm" (
    output(loop.step)
    if loop.step == 'n':
        output(f'On letter [loop.step]')
)