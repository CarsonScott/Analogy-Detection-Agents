# Pre-Analogical Pattern Analysis 
 
### Detectors

A detector is a collection of nodes that receive a set of inputs and produce a nonlinear weighted output. The bias factors are adjusted through lateral inhibition, where a node with high output will attempt to drive down the weights of other nodes, based on how much each weight contributed to their own output. The intent is that a nodes competition- other nodes that respond highly to the same pattern- are reduced because their future responses to that pattern will be weaker. The effect that each node has on another is proportional to its output, so a high output will cause a larger change than a weak output.

### Networks

A network is a collection of detectors that receives a set of inputs and passes it to the first detector. The Remaining detectors each receive outputs from the previous detector to produce their own outputs. The outputs of the last detector make up the outputs of the network as a while.

### Buffers

A buffer is a finite sequence of outputs given by a network over a period of time, where the first element of the sequence contains the most recent output. Buffers are used to represent temporal patterns of activity. Time-series analysis over a network is achieved by passing the contents of a buffer to a different network which observes the sequence the same as it would a spatial pattern. Buffers provide an interface that enables the construction of high-level patterns from collections of lower-level information.
