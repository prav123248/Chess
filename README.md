# Chess

### Description :
The classic board game Chess recreated in Python using PyQt5 for the graphical interface element. Legality and game logic are implemented using object-oriented programming. 


#### Chess (Moving pieces)
<img src="https://user-images.githubusercontent.com/78224090/193458438-97c40fcf-5199-4222-8c4e-63e8d39ed4e6.PNG" width="628" />
In the image above, the black knight has been selected and the program displays which valid tiles it can move to are. These are displayed in green and any tile where a piece can be 
captured is displayed in red.

#### Chess (Only allowing legal moves)
<img src="https://user-images.githubusercontent.com/78224090/193458436-db163875-31c8-4f40-adcf-e2b5c9dcd970.PNG" width="628" />
Alongside identifying the manner in which different pieces move, the game is capable of making additional legality checks to ensure illegal moves are not made. Ordinarily, 
the King can move a single square in any direction but in the case above, the program correctly identifies that the white king cannot move directly left or directly below. These
are illegal moves as the black bishop would check the King if it moved there.

### Technologies used :
    - Python
    - PyQt5 with CSS
    
### Functionalities implemented :
    - A view of the chess board and pieces
    - Chess moving and capturing logic
    - Check and Checkmate logic
    - Removing captured pieces from the graphical interface
    
### Setup :
    (01) - Pip install PyQt5
    (02) - Run __main__.py
