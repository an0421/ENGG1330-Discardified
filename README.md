# ENGG1330-Discardified

Overview:
 
Our game is inspired from the ancient Cantonese game of mah-jong. Having mentioned that, our game features the identification of sets of numbers and the ability to have patience. 
Learning computer science requires an observant eye and a patient mindset. This 4-playergame aims to engage young people interested in the field of computer science and data science so that their observation skills are enhanced, and they tolerate the exasperation that comes with coding.  
While we do not allow the retainment of 10 cards at a time, we reward those with sequences of 3, 4 or 5 numbers. 
Along with teaching you to focus, this game aims to train the ability to foresee losses and profits when it comes to long-term investment. 
Do not underestimate this simple game. It teaches you life skills like nothing else. 
 
We decided to create something we have never seen before to complete the assignment. 
We used the knowledge we learnt through ENGG1330’s previous assignments and coding challenges to create a game that we have never heard of before. 
When our teammate shared her idea, we were very impressed with the creativity behind the game but were challenged by the complexity of it.  
As all of us are relatively new to programming, we required a lot of hard work and perseverance to make this idea a reality. 
Better yet, we took this as a learning opportunity and immediately took on the challenge. Now it is not just a completed assignment, but it is a game we would actually play to relax ourselves. 

Game Rules: 

- DisCARDified is a 4-player card game, which requires you to find sequences of numbers in your deck of cards. After you collect a number of coins, you win.

- We introduce a set of cards, numbered 0-9. There are 4 shapes (Circle, Rectangle, Triangle, Heart). 
- The entire deck of cards will be printed to symbolise the start of the game.

- The first round starts with all the players each getting 4 randomly generated cards.
- The os and time libraries make sure that players don't see each others' cards while playing on the same device.
- Press enter each time as advised.

- Starting from the second round, players check whether they have a sequence of 3 numbers, 4 numbers or 5 numbers at one time. The shape of the card does not affect the sequence throughout the game. 

- Keep pressing enter as instructed to switch players and hide your own cards.

- Players can decide whether to put the cards down in the pool or grab another from home to test their luck. Immediately putting the cards down allows the player to immediately get a score. Holding the sequence will enable you to wait for a number that may extend your sequence and give you more coins.
- For example, you may have 3 4 5 now, but in the next round, you have the possiblity of getting a 2. Hence, you will be able to put 2 3 4 5 in the pool and get extra coins.
 
- In order to put down a sequence of cards, only input the numerical values of the cards, separated by a space i.e. "0 1 2" or "5 6 7".

- When a player doesn't have any sequence on his hand, he has to take one from the home. This process is automated.

- If you find a sequence of 3, you get 3 coins.
- With a sequence of 4, you obtain 5 coins.
- And a holy sequence of 5 gets you 8 coins.

- Note that if any player is caught with 10 cards at a time, the entire game has to restart again. This is the price you pay for getting discardified.
    
- Once a player obtain winning point (4 players*4 = 16), the game will stop after the whole round is finished.
- In case all the cards run out in the process, the game will also end.

- The scores of each player will be tallied at the end of each round.
- If only 1 player not disqualified, he/she will be the winner even he/she haven't obtain the winner point.

- When game is over, if more than 1 players obtain same winning points, the winner is the player who have less cards left.
- The players win if they get the same wining points and no of cards.

- At the end, a heart is printed to console those who did not win.
