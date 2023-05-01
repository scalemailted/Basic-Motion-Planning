# Basic Motion Planning

---

## Project Objectives
What is a C-Space? What is it for a car? What is `SO(3)`? hoe to compute distances in `SO(3)`? What is homeomorphism? What are some examples for homemorphic and non-homemorphic subspaces? Follow a geometric path from D* algorithm from [Dstar-Pathfinding-Simulations](https://github.com/scalemailted/dStar-Pathfinding-Simuations) project using a quadcopter (UAV).

---

## Motivations
This project covers fundamental concepts for motion planning orientation and trajectory. It bridges the gap from path planning to motion planning, beginning with C-space and its applications. The use of special orthogonal groups, including `SO(3)`, is explored to compare orientations and differentiate motion planning from path planning. Homeomorphism is introduced to explain the mapping between geometric space and C-space. Finally, a practical, applicable examples of motion planning is provided in CoppeliaSim.

---

## Approach

TODO add explanation about the approach taken in a general and abstract way
---

## Key Features

TODO list items that covered in this project

---

## Algorithmic Overview:

TODO detail the algorithm breakdown in plain english way for code
---

## Implementation: 

### *CoppeliaSim* 

**simple-motion-planning.ttt**
> Tbd

![Demo: CoppeliaSim](./assets/coppeliasim.gif)

**orientation-motion-planning.ttt**
> Tbd

![Demo: CoppeliaSim](./assets/coppeliasim.gif)

---

## Project Hierarchy 
- 📁 **assets/**
    >*contains all images in readme documentation*
- 📁 **coppeliasim/**
    + 📁 **scenes/**
        >*contains CoppeliaSim scenes (.tt)*
        - 📄 multiagent-avoidance.tt
    + 📁 **scripts/**
        >*contains associated Python scripts from the scene*
        - 📄 dstar_path.py
            >*dstar path planning algorithm*
        - 📄 motion_planner.py
            >*motion planning algorithm with targets and wheeled robots*
        - 📄 robot1.py
            >*policy for avoiding other dynamic obstacles*
        - 📄 robot2.py
            >*policy for avoiding other dynamic obstacles*