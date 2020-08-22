LEFT_TOP, RIGHT_BOTTOM, DECOMPOSE = None, None, None

three_lights = {
    "one": 2,
    "two": 1,
    "three": 1,
    "four": 1
}

three_lights_q = {
    "one": 14,
    "two": 21,
    "three": 1000,
    "four": 21
}

wind = {
    "one": 21,
    "two": 50,
    "three": 60,
    "four": 4
}

wind_q = {
    "one": 21,
    "two": 20,
    "three": 6,
    "four": 400
}

witcher = {
    "one": 400,
    "two": 1,
    "three": 9,
    "four": 400
}

devices = {1: "magic", 2: "free"}

device = devices[1]

DIABLO_ROLE = wind

if device == "magic":
    LEFT_TOP = [1165, 450]
    RIGHT_BOTTOM = [1530, 690]
    DECOMPOSE = [125, 225]
elif device == "free":
    LEFT_TOP = [1455, 560]
    RIGHT_BOTTOM = [1905, 860]
    DECOMPOSE = [150, 300]
