# Pre-Analogical Pattern Learning 
 
### Layers

A layer is a collection of nodes that receive a set of inputs and produce a nonlinear weighted output. The bias factors are adjusted through lateral inhibition, where a node with high output will attempt to drive down the weights of other nodes, based on how much each weight contributed to their own output. The intent is that a nodes competition- other nodes that respond highly to the same pattern- are reduced because their future responses to that pattern will be weaker. The effect that each node has on another is proportional to its output, so a high output will cause a larger change than a weak output.

### Networks

A network is a collection of layers that receives a set of inputs and passes it to the first layer. The Remaining layers each receive outputs from the previous layer to produce their own outputs. The outputs of the last layer make up the outputs of the network as a while.
