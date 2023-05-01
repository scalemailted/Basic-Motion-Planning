# Basic Motion Planning

---

## Project Objectives
TODO add explanation about project objectives

---

## Motivations
TODO add explanation about motivations concepts

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

**basic-motion-planning.tt**
> Tbd

![Demo: CoppeliaSim](./assets/coppeliasim.gif)

**basic-motion-planning-orientation.tt**
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