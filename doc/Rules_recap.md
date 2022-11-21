# Rules

## Beginning of the game : 

Each Player starts with : 

- 6 pieces with each 3 caracteristics [speed, attack_strength, defense_strength] :   
2 x regular player [3, 0, 0]  
1 x big guy [2, 2, 1]  
1 x tough guy [3, 1, 0]  
1 x fast guy [4, -1, -1]  
1 x smart guy [3, 0, 1]  

- 6 strength cards : [1, 2, 3, 4, 5, 6]

- Each player places its pieces however he wants on the 2 first lines of his side

- One strength card is randomly picked to know where the ball is placed at the beginning

- One player is randomly picked to start

## End of the game

The game is over when one of the player crosses the final line with the ball.

## Special Cases

#### FACE OFF
each player picks a strength card (which will be discarded after)  
This card is added to the strength (attack or defense) of the piece  
The piece with the most points wins

#### TURNED OVER
When a piece is turned over, it cannot move in the next round

## One round

During one round, a player can : 

### - move one or two players according to their number of cases allowed
if a player B from the other team is in the way of the player A : FACE OFF   
 if A wins, he can continue (he cannot stop on B's case), B is TURNED OVER  
 if B wins, A is TURNED OVER and the ball is placed behind him


### - do as many passes as he wants 
only behind the player [x-1 : x-2, y-2 : y+2]  
if a player B from the other team is between the player A and the receiver : FACE OFF    
 if B (defense) wins, he takes the ball but A can keep playing (ex : tackle)  
 if A (attack) wins, the pass is succesful  


### - tackle the piece B with the ball (this ends the round)
possible with one or two pieces  
the pieces have to have the right number of movements  
at the end, the striker A will go back to his initial position  
FACE OFF    
if B wins, B keeps the ball, A is TURNED OVER  
if A wins, B is TURNED OVER and :   
  if A.score > B.score + 2 : A takes the ball  
  if B is on his "ligne d'en but" : he puts the ball next to him on the oposite side from A  
  else : the ball is placed behind B   
  (if a player is where the ball ends up, he takes the ball, otherwise, the next player to come here will take the ball)   

### - do a "coup de pied à suivre" (counts as a pass and not as a movement)
if no player from the team is stricktly in front  
the ball can be sent in front in a rectangle : [x+1 : x+3, y-3 : y+3]  
the first player to go to this square takes the ball

### - score a try (this ends the game)
when a piece with the ball has enough movements to go through the final line, the game is over
