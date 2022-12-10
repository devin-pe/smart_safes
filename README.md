# Smart Safes 

Smart Safes is a prototype of a system for storing and managing passwords securely.

## Installation

To install Smart Safes, clone the repository and run the following command:
```
$ pip install -r requirements.txt
```
## Usage

To run Smart Safes, use the following command:
```
$ python vault.py
```
To experiment with the time-taken between successful and unsuccessful decryption, comment out the demo in `vault.py`
use the following command:
```
$ python results.py
```

## Code Structure

This project is organized into the following directories and files:

- `README.md`: This file contains an overview of the project and instructions for getting started.
- `requirements.txt`: This file contains the dependencies for the project.
- `vault.py`: This file contains the `Vault` class and demo function
- `decoys.txt`: This file contains the decoy passwords obtained from the pcfg cracker library used in `vault.py`
- `results.py`: This file contains functions for determining the time difference between successful and unsuccessful decryptions
- `plaintexts/`: This directory contains sample password list plaintexts used in `results.py`
    - `short.txt`: This file contains 6 sample passwords
    - `medium.txt`: This file contains 25 sample passwords
    - `large.txt`: This file contains 54 sample passwords

## Acknowledgments

I would like to give credit to the author of this repository for generating the decoy passwords: 
- https://github.com/lakiw/pcfg_cracker




