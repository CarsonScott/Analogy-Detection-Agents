# Multi-Agent System for Learning Analogous Patterns  

Agents range from very simple to the very complex, operating as simple functions without memory space to intelligent actors that take control of other agent’s behavior at will. Despite the obvious difference in functionality, information processed by all agents originates from the same environment: A graph. 

Data flows into the system from the most simple agents moving around on the graph and passes all the way to the most complex, who make decisions and delegate tasks to lower levels. The bottom-level agents receive subgraphs of their local environments as input. Values submitted as output by each bottom-level agent represent neighboring nodes that they takes a step toward, changing their position on the graph by one.

***

# 1) Simple Agents

__1.1 Movers__

A mover is an agent that takes walks in a graph. Movers have simple graphs that are called templates, which they compare to their local neighborhood at each step to find how closely its current environment state matches some ideal state. Outputs are behaviors that are chosen to move an agent in the direction of highest similarity.

__1.2 Pushers__

A pusher is an agent that impacts the behavior of a mover. Pushers have biases called weights that alter the errors calculated by a mover in order to emphasize certain elements of the mover’s template over others. Outputs are the weighted errors that are sent back to a mover where they override the calculation and are used to make decisions.

__1.3 Revisers__

A reviser is an agent that adjusts the properties and weights of a mover and pusher. Revisers have incremental values called learning rates that effect the magnitude of the changes. Outputs are deltas that are sent to a mover/pusher where they’re added to the properties/weights and reduce the distance between their current values and a set of target values calculated by the reviser.

![](https://github.com/CarsonScott/Analogy-Detection-Agents/blob/master/img/simple%20agents.png)
