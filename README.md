# Rubiks-Cube-planners-comparison

Comparison of planners for solving the Rubik's Cube problem.

## Honors

Project published in the Planning And Reasoning course site: https://sites.google.com/uniroma1.it/pr-23-24/ct-team

## Planners

- Scorpion 2023
- Fast-Downward IDA* + add heuristic
- Fast-Downward IDA* + hmax heuristic
- Fast-Downward IDA* + ff heuristic

## Requirements

Download submodules:

    git submodule init
    git submodule update

Install apptainer (Ubuntu):

    sudo apt update
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:apptainer/ppa
    sudo apt update
    sudo apt install -y apptainer

Download Fast Downward image:

    mkdir fast-downward
    apptainer pull ./fast-downward/fast-downward.sif docker://aibasel/downward:latest

## Dependencies

Rubiks cube generator: https://github.com/ipc2023-classical/domain-rubiks-cube

Planner: https://github.com/ipc2023-classical/planner25

## Developer commands

Build Scorpion planner:

    cd planner25
    sudo apt install cmake g++ git make python3
    ./build.py
    sudo apptainer build scorpion.sif Apptainer.scorpion_2023

Run optimal-solver:

    cd domain-rubiks-cube/optimal-solver
    python3 pddl-to-solver-input.py ../../problems/problem15.pddl
    make
    ./optimal-solver

then enter the output of pddl-to-solver-input.py






