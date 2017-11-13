In this project, I use a genetic algorithm to evolve a tic-tac-toe playing neural network.

The network size is fixed.<br>
Input layer 18 units: 2 units to represent each game cell, as each game cell has 3 possible states - blank, player occupied, opponent occupied.<br>
Hidden layer 128 units with relu activation: Should be enough to play a perfect tic-tac-toe.<br>
Output layer 9 units: 1 unit for each game cell.<br>

The weights and bias units are updated through a genetic algorithm.
Each round of evolution pits 40 neural networks against each other in a round-robin format to determine fitness, where a loss is +1 fitness, a draw is 0, and a loss is -1.
The 40 networks which will pass to the next round are drawn from the following:
- the top few networks with the highest fitness
- randomly selected networks from the remaining networks
- new, randomly generated neural networks
- random crossovers, where the weights of a few units in one neural network are swapped with the weights of an equal number of units in another neural network
- mutation, where random weights are modified

After 200 rounds of evolution, the neural network with the highest fitness is pit against 49 randomly generated neural networks in a round-robin format. This network usually outperforms most of the randomly generated networks, but is still far from playing a perfect game.

The algorithm can probably evolve a network which plays a perfect game given enough time and parameter tuning, though I feel that gradient descent would be a better way to tune the weights in this case. 

Also, I'm not sure if evolving the networks actually helped to tune the parameters. 
A basline comparison would be that in each evolution, we select 
- the top few networks with the highest fitness
- randomly generate all other neural networks

I have not compared this with the current implementation, but doing so would give us a better idea of whether evolution really helped here.

Next up: using genetic algorithms to determine network architecture instead?
