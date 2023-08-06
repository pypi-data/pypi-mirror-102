# wTermUi
wTermUi is a simple module that allows creating good looking terminal uis.
It's very easy to use and doesn't rely too much on other libraries.

## Usage

Any wTermUi window is navigated using:
Up arrow, Down arrow, Left arrow, Right arrow
where up arrow navigates to the previous input widget (Button, Switch, TextBox),
and down arrow navigates to the next input widget (Button, Switch, TextBox).

Left arrow navigates to the previous page, and right arrow navigates to the next page.

When you press enter, the currently selected input widget will be activated.
In the case of inputs, you'll be prompted to assign a new value, while buttons
just run their callback function, and switches just toggle.

## Changelog

### V 0.0.2.2
 + Added allow_scaling, adjust_term_size to TermWin class
 + Changed ui by a bit
 + Inputs/TextBoxes are more stable

### V 0.0.2.1
 + Fixed wTermUi not importing correctly 

## Documentation

All widgets, except for Switches, have 2 required arguments: pos, text/placeholder_text.

pos takes 3 arguments, x, y, and page.
x represents which character on the x axis, not which pixel, same goes for y.
Page is which page to put this widget on.

text/placeholder_text is just any string. Note that the widget scales with the length of text/placeholder_text.

Optinal argument is callback, it will toggle whenever the current widget changes in any way.

The currently supported widgets are:
```py
Label(
    pos=[x, y, page],
    text="Label"
)

TextBox(
    pos=[x, y, page],
    placeholder_text="TextBox",
    callback=None
)

Button(
    pos=[x, y, page],
    text="Label",
    callback=None
)

Switch(
    pos=[x, y, page],
    callback=None
)
```

Creating a window is very simple. Just call 
```py
window = TermUi(
    win_size=[size_x, size_y],
    win_title="wTermUi window",
    max_pages=1, # optional
    key_events=None # optional
    border_letters="╚╔╩╦╠═╬╝╗║╣" #optional
)
```

this code will return a window that you can add widgets to using
```py
window.add_widget(Widget(
    # Widget arguments
))
```

where widget can be any of teh widgets mentioned above.
This function returns the cerated widget, so you can retrieve 
data such as text or toggled from them.

```py
textbox = window.add_widget(TextBox([0,0,1],"Enter text here"))
print(textbox.text)
```

The code above will print whatever teh user put in. 
Note that text and placeholder_text are different values.

## Example codes

Here's an example code for a calculator:
```py
from wTermUi import *
import math

window = TermWin([41, 20], "Calculator", 2)


def convert_numbers():
    if str.lower(number1.text) == "pi":
        number1.text = "3.1415626"
    if str.lower(number2.text) == "pi":
        number2.text = "3.1415626"


def convert_number():
    if str.lower(number3.text) == "pi":
        number3.text = "3.1415626"


def add_numbers():
    convert_numbers()
    output.text = "Output: " + str(float(number1.text) + float(number2.text))


def sub_numbers():
    convert_numbers()
    output.text = "Output: " + str(float(number1.text) - float(number2.text))


def mul_numbers():
    convert_numbers()
    output.text = "Output: " + str(float(number1.text) * float(number2.text))


def div_numbers():
    convert_numbers()
    if float(number2.text) != 0.0:
        output.text = "Output: " + str(float(number1.text) / float(number2.text))


def pow_numbers():
    convert_numbers()
    output.text = "Output: " + str(float(number1.text) ** float(number2.text))


def mod_numbers():
    convert_numbers()
    output.text = "Output: " + str(float(number1.text) % float(number2.text))


def fulldiv_numbers():
    convert_numbers()
    output.text = "Output: " + str(float(number1.text) // float(number2.text))


def sqrt_number():
    convert_number()
    output2.text = "Output: " + str(math.sqrt(float(number3.text)))


def sin_number():
    convert_number()
    output2.text = "Output: " + str(math.sin(float(number3.text)))


def cos_number():
    convert_number()
    output2.text = "Output: " + str(math.cos(float(number3.text)))


window.add_widget(Label([0, 0, 1], "Number 1: "))
number1 = window.add_widget(TextBox([11, 0, 1], "INSERT NUMBER HERE"))

window.add_widget(Label([0, 3, 1], "Number 2: "))
number2 = window.add_widget(TextBox([11, 3, 1], "INSERT NUMBER HERE"))

window.add_widget(Label([0, 0, 2], "Number: "))
number3 = window.add_widget(TextBox([9, 0, 2], "INSERT NUMBER HERE"))

window.add_widget(Button([0, 6, 1], "+", add_numbers))
window.add_widget(Button([4, 6, 1], "-", sub_numbers))
window.add_widget(Button([8, 6, 1], "*", mul_numbers))
window.add_widget(Button([12, 6, 1], "/", div_numbers))
window.add_widget(Button([16, 6, 1], "^", pow_numbers))
window.add_widget(Label([0, 7, 1], "Advanced operations: "))
window.add_widget(Button([0, 8, 1], "%", mod_numbers))
window.add_widget(Button([4, 8, 1], "//", fulldiv_numbers))


window.add_widget(Button([0, 3, 2], "√", sqrt_number))
window.add_widget(Button([4, 3, 2], "sin", sin_number))
window.add_widget(Button([10, 3, 2], "cos", cos_number))

output = window.add_widget(Label([0, 12, 1], "Output: "))
output2 = window.add_widget(Label([0, 12, 2], "Output: "))

window.main_loop()
```