# Conway's Game of Life with a stochastic twist

# Rules

A square-lattice holds cells.
Every cell is in one of two states: alive (`1`) or dead (`0`).
Every cell has eight neighbors.

Consider `state_1` and `state_2` where `state_2` is obtained by applying the time-propagation rules (from Wikipedia):

 - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
 - Any live cell with two or three live neighbours lives on to the next generation.
 - Any live cell with more than three live neighbours dies, as if by overpopulation.
 - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Stochastic term: breaking the rules
Any cell that is bound to be changed by the propagation rules is a rule breaker candidate.
Cells that do not change from state the rules are not rule-breaking candidates.
this means a stable unchanging system cannot spontenously break-out.

However, "stable" oscilators or sliders can spontaneaously change into soemthings else.
For every potentle cell change during a time-propagation operation a centered Gaussian random variable with standard deviation `kT`  is created.
The variable is squared and compared to 1.0. 
If it is less that 1.0 the regular rules are repsected and the change occurs.
If it is more that 1.0 the change is ignored and the cell's state is preserved.



# Quick-start
```bash
python3 run.py
```
