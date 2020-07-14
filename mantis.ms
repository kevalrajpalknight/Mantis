import some_package

function hello -- x, y, z (
    stuff = x + y + z
    return stuff
)

loop int 37 (
    output(hello(loop.step, 1, 2))
)

output(location.line)

loop char: str "qwertyuiopasdfghjklzxcvbnm" (
    output(loop.step)
    if loop.curr_step == 'n':
        output(f'On letter [loop.cuur_step]')
)