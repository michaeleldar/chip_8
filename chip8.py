import renderer, datetime

rend = renderer.Renderer()

loop = ""

fps = 60

fpsInterval = ""

startTime = ""

now = ""

then = ""

elapsed = ""


def init():
    global then, fpsInterval, startTime
    fpsInterval = 100 / fps
    then = datetime.datetime.now()
    startTime = then

    # TESTING CODE
    rend.testRender()
    rend.render()
    # END OF TESTING CODE


def step():
    now = datetime.datetime.now()
    elapsed = now - then

    if elapsed.total_seconds() > fpsInterval:
        pass  # CPU CYCLE


init()
while True:
    step()
