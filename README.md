# Matrix

![Matrix](http://assets.b9.com.br/wp-content/uploads/2009/07/matrix1.jpg)


## Installation

    $ pip install -r requirements.txt

## Tests
To running tests execute the follow command:

    $ py.test

## Debugging

To show the output after any command, run this on your console:

    $ export DEBUG_MATRIX=1

## Running the application
To run the application execute:

    $ python app.py

### Program instructions

    I M N

Create a matrix MxN.

    C

Clear the Matrix.

    L X Y C

Put the color C in the `(x,Y)` position.

    V X Y1 Y2 C

Put the color C vertically in `(X, Y1-Y2)`.

    H X1 X2 Y C

Put the color C horizontally in `(X1-X2, Y)`.

    K X1 Y1 X2 Y2 C

Create a rect in (X1-X2, Y1-Y2) with the C color.

    F X Y C

Fill a line vertically and horizontally if exists two points in the same direction.

    S name

Save to the `name` file.

    X

Close the program.
