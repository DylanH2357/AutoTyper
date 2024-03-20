import json
import time as t
import keyboard as k
import sys

'''

sudo python3 path_to_your_file

'''

def suppress_keyboard():
    keyCode = "left_shift"  # KeyCode #1
    false = False
    # Define the path to the Karabiner JSON file
    karabiner_file_path = "path_to_your_file/karabiner.json"
    new_rule = {
    "description": "Fast Key Press",
    "manipulators": [
        {
            "from": {
                "key_code": "a",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "a"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "b",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "b"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "c",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "c"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "d",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "d"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "e",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "e"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "f",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "f"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "g",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {

            "from": {
                "key_code": "g"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "h",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "h"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "i",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "i"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "j",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "j"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "k",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "k"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "l",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "l"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "m",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "m"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "n",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "n"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "o",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "o"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "p",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "p"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "q",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "q"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "r",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "r"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "s",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "s"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "t",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "t"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "u",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "u"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "v",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "v"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "w",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "w"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "x",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "x"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "y",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "y"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "z",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "z"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "0",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "0"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "1",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "1"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "2",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "2"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "3",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "3"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "4",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "4"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "5",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "5"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "6",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "6"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "7",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "7"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "8",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "8"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "9",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "9"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "spacebar",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "spacebar"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "slash",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "slash"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "delete_or_backspace",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "delete_or_backspace"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "comma",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "comma"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "period",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "period"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "close_bracket",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "close_bracket"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "open_bracket",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "open_bracket"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "backslash",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "backslash"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "quote",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "quote"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "semicolon",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "semicolon"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "equal_sign",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "equal_sign"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "hyphen",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "hyphen"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "grave_accent_and_tilde",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "grave_accent_and_tilde"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "left_option",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "left_option"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "return_or_enter",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "return_or_enter"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "tab",
                "modifiers": {
                    "mandatory": [
                        "any"
                    ]
                }
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "tab"
            },
            "to": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "to_if_held_down": [
                {
                    "key_code": keyCode,
                    "repeat": false
                }
            ],
            "type": "basic"
        }
    ]
}

    with open(karabiner_file_path, "r") as file:
        data = json.load(file)
    # Update the "rules" portion with the new rule
    data["profiles"][0]["complex_modifications"]["rules"].append(new_rule)
    # Write the modified JSON back to the file
    with open(karabiner_file_path, "w") as file:
        json.dump(data, file, indent=4)


def regain_keyboard():
    karabiner_file_path = "/Users/dylanhackos/.config/karabiner/karabiner.json"
    with open(karabiner_file_path, "r") as file:
        data = json.load(file)
    # Set the "rules" portion to an empty list
    data["profiles"][0]["complex_modifications"]["rules"] = []
    # Write the modified JSON back to the file
    with open(karabiner_file_path, "w") as file:
        json.dump(data, file, indent=4)


def main_program():  # main program function
    print("The program will begin when the control key is pressed twice within a second...")
    ctrl_pressed_time = 0
    ctrl_pressed_count = 0
    right_shift_pressed_time = 0
    right_shift_pressed_count = 0
    command_pressed_time = 0
    command_pressed_count = 0

    while True:
        event = k.read_event()
        if event.event_type == "down":  # check for key press
            if event.name == "ctrl":
                current_time = t.time()
                # Check if it's within 1 second since the last ctrl press
                if current_time - ctrl_pressed_time <= 1:
                    ctrl_pressed_count += 1
                else:
                    ctrl_pressed_count = 1
                ctrl_pressed_time = current_time
                # If ctrl pressed twice within a second
                if ctrl_pressed_count == 2:
                    print("Starting program")
                    break

    suppress_keyboard()

    texts = {
        "text1": "Have you ever wondered about your heritage and where you come from? In Lorraine Hansberry’s A Raisin in the Sun, Beneatha is an African-American woman who lives in a white society and struggles to preserve her heritage. As a result, Beneatha finds herself confronted with a choice of either assimilating into white culture or conserving her African heritage. In the play, A Raisin in the Sun, Lorraine Hansberry uses Beneatha’s interactions with George, Asagai, and Walter to provide her perspective on the complexities of assimilation and the importance of preserving one’s heritage. To begin with, Beneatha’s relationship with George and Asagai conveys the struggle to preserve her heritage. For instance, Beneatha finds herself in an argument with George about her heritage. She states, “[Assimilationist] means someone who is willing to give up his own culture and submerge himself completely in the dominant, and in this case oppressive culture!” (Hansberry 81). The passage begins with Beneatha's definition of being an assimilationist. She characterizes the term as someone who willingly abandons their heritage to fit in with the dominant culture, which she describes as being oppressive. This conveys Beneatha’s current view of assimilation as voluntarily conforming to the dominant or oppressive culture. The passage also suggests that there's a trade-off between assimilation and heritage. When in the pursuit of assimilation, heritage is lost. Similarly, when energy is being used to preserve heritage, assimilating into the dominant culture is delayed. Furthermore, Beneatha’s perspective on assimilation mirrors the author's beliefs as she emphasizes the importance of preserving one’s heritage. This is because the tension between assimilation and heritage is repeated throughout the play. Conversely, Asagai attempts to prevent Beneatha from assimilating into white culture by inviting her to go to Africa. He states, “Three hundred years later the African Prince rose out of the seas and swept the maiden back across the middle passage over which her ancestors had come…Nigeria. Home…I will show you our mountains and our stars; and give you cool drinks from gourds and teach you the old songs and the ways of our people—and, in time, we will pretend that…you have only been away for a day” (Hansberry 135). Here, Asagai invites Beneatha to abandon assimilation and move with him to Africa to live her true identity as an African woman. He invokes Nigeria as their “home”, praises the beauty of their native land, and attempts to sweep her off her feet. Asagai reminds her that although 300 years have passed since Beneatha’s ancestors were taken as slaves, “we [can] pretend that…you have only been away for a day” (135). Hansberry uses this scenario to demonstrate the power of having the choice to return to one’s heritage and abandon the idea of assimilation. Additionally, Beneatha’s interactions with her brother Walter demonstrate the complexities of assimilation and the conflict of preserving her heritage. For example, Walter confronts Beneatha regarding her aspirations of becoming a doctor while in an argument with her. He states, “Who the hell told you you had to be a doctor? If you so crazy ’bout messing ’round with sick people—then go be a nurse like other women—or just get married and be quiet …” (Hansberry 38). Here, Walter tells Beneatha that he wants her to assimilate into white culture by “[being] a nurse like other women” (38). He implies that she should abide by the expectations of the dominant culture by becoming a nurse and being submissive. Beneatha’s pressure to assimilate demonstrates that assimilation isn’t just external, but that it can also come from family. Furthermore, Walter states that Beneatha should “get married and be quiet” (38). Walter not only reinforces the pressure to assimilate, but it highlights the gendered aspect of assimilation. He urges Beneatha to embrace a more traditional gender role as a way to assimilate into the dominant culture. This illustrates the common complexities of assimilation and the difficulty of maintaining one’s heritage. Walter’s anger toward Beneatha also helps reveal Hansberry’s disapproval of assimilation. This can be seen in the contrasting roles she assigns to Walter and Beneatha. Walter is seen in a negative light and represents pressure to conform to the dominant culture, while Beneatha plays the protagonist's role, demonstrating the struggle to preserve her heritage. Some people may say that assimilation is beneficial to people because it allows them to fit into the dominant culture. However, merely fitting into a culture doesn't necessarily provide any benefits; instead, the disadvantages of assimilation significantly outweigh any potential advantages. For instance, as individuals embrace a new culture, they feel compelled to let go of their customs and traditions. As a result, they may feel a sense of disconnect from their identity, leading to feelings of confusion and isolation. In A Raisin in the Sun, Lorraine Hansberry used Beneatha’s encounters with George, Asagai, and Walter to elaborate on the challenges of assimilation and the importance of maintaining one’s heritage. When Beneatha interacts with George, she is pressured to assimilate into the dominant culture around her, while Asagai represents choosing to live fully in one’s heritage by returning to one’s place of ancestry. The play gives us thought-provoking insight into how a minority culture can struggle to feel like part of the dominant society while also maintaining its unique heritage. (893 words)",
        "text2": "This is text #2, and that's pretty cool",
        "text3": "This is text #3, and that's pretty cool",
        "text4": "This is text #4, and that's pretty cool",
        "text5": "This is text #5, and that's pretty cool",
        "text6": "This is text #6, and that's pretty cool",
        "text7": "This is text #7, and that's pretty cool",
        "text8": "This is text #8, and that's pretty cool",
        "text9": "This is text #9, and that's pretty cool",
        "text10": "This is text #10, and that's pretty cool",
        "text11": "This is text #11, and that's pretty cool",
        "text12": "This is text #12, and that's pretty cool",
        "text13": "This is text #13, and that's pretty cool",
        "text14": "This is text #14, and that's pretty cool",
        "text15": "This is text #15, and that's pretty cool",
        "text16": "This is text #16, and that's pretty cool",
        "text17": "This is text #17, and that's pretty cool",
        "text18": "This is text #18, and that's pretty cool",
        "text19": "This is text #19, and that's pretty cool",
        "text20": "This is text #20, and that's pretty cool"
    }

    paused = False
    i = 0  # initial value of i (place value in text)
    j = 0  # initial value of j (the specific text you are in)
    while i < 100000:
        event = k.read_event()
        if event.event_type == "down":  # check for key press      
            # for pausing the program
            if event.name == "ctrl":
                current_time = t.time()
                # Check if it's within 1 second since the last ctrl press
                if current_time - ctrl_pressed_time <= 1:
                    ctrl_pressed_count += 1
                else:
                    ctrl_pressed_count = 1
                ctrl_pressed_time = current_time
                # If ctrl pressed twice within a second
                if ctrl_pressed_count == 2 and paused == False:  # if not paused
                    print("Pausing Program")
                    regain_keyboard()
                    paused = True  # now paused
                elif ctrl_pressed_count == 2 and paused == True:  # if paused
                    print("Resuming Program")
                    suppress_keyboard()
                    paused = False  # now unpaused

            # for exiting the program
            if event.name == "right shift":
                current_time = t.time()
                # Check if it's within 1 second since the last right shift press
                if current_time - right_shift_pressed_time <= 1:
                    right_shift_pressed_count += 1
                else:
                    right_shift_pressed_count = 1
                right_shift_pressed_time = current_time
                # If right shift pressed twice within a second
                if right_shift_pressed_count == 2:
                    print("Exiting Program")
                    regain_keyboard()
                    sys.exit()
                    
            # for switching between texts: (command)
            if event.name == "command":
                current_time = t.time()
                # Check if it's within 1 second since the last return press
                if current_time - command_pressed_time <= 1:
                    command_pressed_count += 1
                else:
                    command_pressed_count = 1
                command_pressed_time = current_time
                # If return pressed twice within a second
                if command_pressed_count == 2:
                    print("Switching Texts")
                    if j == 19:
                        j = -1  # reset to text #1
                    i = 0  # go to the beginning of the text
                    j += 1

            if paused == False and not event.name == "ctrl" and not event.name == "command" and not event.name == "right shift" and not event.name == "up" and not event.name == "down" and not event.name == "right":
                k.write((texts[(list(texts.keys())[j])][i]), delay=0, restore_state_after=True, exact=None)
                print(i)
                i += 1

    regain_keyboard()

try:
    main_program()

except:
    regain_keyboard()

'''

sudo python3 path_to_your_file/KeyboardRemapping.py

'''
