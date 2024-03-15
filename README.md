# Rubiks-Cube-planners-comparison

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

Build Scorpion planner:

    cd planner25
    apptainer build scorpion.sif Apptainer.scorpion_2023

## Dependencies

Rubiks cube generator: https://github.com/ipc2023-classical/domain-rubiks-cube

Planner: https://github.com/ipc2023-classical/planner25





