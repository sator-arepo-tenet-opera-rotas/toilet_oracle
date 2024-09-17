# toilet_oracle
ON TONIGHT'S EPISODE OF WILL IT FLUSH?! ... WILL IT FLUSH?!?
  _
  Turn 1
  Applying wind force: 0.45, wave force: -0.89
  Sailor Left decides to apply base pressure to maintain balance.
  Sailor Left applying base pressure: 2.45 on left side
  Sailor Right decides to apply base pressure to maintain balance.
  Sailor Right applying base pressure: 2.30 on right side
  Boat tilt angle: -0.94 degrees

  Turn 2
  Applying wind force: -0.38, wave force: 0.27
  Sailor Left decides to add more chemical pressure.
  Sailor Left adding chemical pressure: 1.29 on left side
  Sailor Right decides to add more chemical pressure.
  Sailor Right adding chemical pressure: 1.41 on right side
  Boat tilt angle: -0.85 degrees
  ...
  Boat capsized by right side!
_

Base Case (DOF 1): Simple balance control. Each sailor applies a weight (pressure) on their side. It's a basic system solvable in polynomial time, similar to the Knapsack problem, where the goal is to balance the boat by ensuring equal weight on both sides.

DOF 2: Chemical pressure. Sailors add chemicals to the water that influence the overall weight distribution. The problem gets more complex as the chemicals interact, requiring additional calculations for fluid dynamics. This makes the problem harder than the base case.

DOF 3: Chemical Reactions. The sailors not only use chemicals but also initiate chemical reactions that introduce dynamic pressures (expansions or contractions). This adds an exponential increase in complexity, requiring real-time adjustment for both sides to maintain balance.

DOF 4: Environmental Factors (Wind, Waves, etc.). These external factors add noise to the system, making it exponentially harder to predict and balance the boat.

DOF 5: Optimization of Sailor Actions. The sailors must optimize their actions based on the boat's dynamic state, requiring them to solve an NP-hard-like problem in real-time, such as calculating the optimal moment and type of chemical to add.
