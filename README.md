# Matrix

![Matrix](http://assets.b9.com.br/wp-content/uploads/2009/07/matrix1.jpg)


## Installation

    $ pip install -r requirements.txt

## Tests
To running tests execute the follow command:

    $ py.test

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

Put the color C vertically in `(X1-X2, Y)`.

    K X1 Y1 X2 Y2 C

Put the color C vertically in (X1-X2, Y1-Y2).

    F X Y C

Fill (pending).

    S name

Save to the `name` file.

    X

Close the program.
