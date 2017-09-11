# Analogous Pattern Learning in Multi-Agent Systems

Agents in a system, ranging from elementary to complex in function, can effectively be used as a method of pattern recognition, which not only learns but also generalizes information from concrete examples in realtime. Agents can be anything from a simple function with no memory to an intelligent automata who takes control of other agent’s behavior to achieve its own goals. Despite the operational variations, each agent processes information from the same source: a graph that makes up the system environment.

The simplest form of agent has a position in the environment for which it can move by taking steps to neighboring nodes in the graph. It makes observations of the local neighborhood which are received as inputs and passed to higher-level agents who perform more complex operations on the data before sending it even higher in the system. The bottom-level outputs are value representing neighbors of the agents, to which each one takes a step and changes their position in the environment. 

***

# 1) Simple Agents

__1.1 Movers__

A mover is an agent that takes walks in a graph. Movers have simple graphs that are called templates, which they compare to their local neighborhood at each step to find how closely its current environment state matches some ideal state. Outputs are behaviors that are chosen to move an agent in the direction of highest similarity.

__1.2 Pushers__

A pusher is an agent that impacts the behavior of a mover. Pushers have biases called weights that alter the errors calculated by a mover in order to emphasize certain elements of the mover’s template over others. Outputs are the weighted errors that are sent back to a mover where they override the calculation and are used to make decisions.

__1.3 Revisers__

A reviser is an agent that adjusts the properties and weights of a mover and pusher. Revisers have incremental values called learning rates that effect the magnitude of the changes. Outputs are deltas that are sent to a mover/pusher where they’re added to the properties/weights and reduce the distance between their current values and a set of target values calculated by the reviser.

![](https://github.com/CarsonScott/Analogy-Detection-Agents/blob/master/img/simple%20agents.png)
