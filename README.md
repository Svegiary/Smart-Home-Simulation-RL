# ai2cyber small project

## Overview

This is a simple Smart Home Simulation project. The implementation supports building a home that has room, 
each room has devices and sensors and a human inside. The goal of this project is to train an ai agent
that takes the right actions to maximize user comfort and minmize power consumption.

There are external variables such as outside temp, outside humidity and sunlight that affect the internal measurements

#### Patterns Used: Strategy , State , ~~Observer~~ , Command , Singleton , Factory

## Structure

### Device
There are 3 devices. A **light** , an **AC** and a **Dehumidifier**. A user can control these devices in order to achieve efficiency and comfort.
Each device has a unique influence on the simulation combined with external variables.

To create a device there is a **DeviceFactory** class for seperating the creation logic in case it becomes complex

### Device Commands
Each device is responsible for handling its own state and for providing a control interface. However the actual command execution is handled by the invoker. 
Each device has classes that represent commands. Then the command can be executed by the invoker , that also keeps a history of all executed commands

Through the **CommandFactory** class , when all devices have been created and placed inside a home, commands are created for each one and the all can be accessed through a list inside the class

### Room
Each room has devices and ~~sensors~~. The room class can be used to attaching and detaching devices to itself while also indicating if a human is inside it

### Home

A home class represents the home structure. It contains all the rooms , information about the internal temp , humidity and luminance and a human that can be placed with a function to a room

You create the home through the **HomeFactory** class

### Simulation

#### Config
You can configure simulation parameters such as duration , time intervals , max allowed temp (you can achiece 100c inside temp) etc through the config class
 
Sample usage inside the **main.py** file

#### Simulation class
The simulation class holds info such as the config files , the generated environment data , the home , the runtime plan and the timestamps needed for external data generation and indexing

It also has a method for extracting a simulation snapshot that takes into account the device and the outside variables influence for calculating the next state

#### Simulation Snapshot

This class has the logic for calculating the internal state of the house

### Data Generation and calculation

#### Generation
For the scope of this project I am generating data in the following format
1. I generate timestamps based on the duration of the simulation and the time interval specified in the config file
2. All data will first rise in value and then fall again . Ex. the temp will start at 10c , rise to 30c and then fall back to 10c.

#### Calculation

For calculating the inside state of the house I take into account both the device influence and the influence from the environment. There are more details inside the corresponding files 
