# Curiosity Global Exchange

Curiosity Global Exchange aims to improve liquidity between traditional financial instruments (FICC) and cryptocurrencies. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
- Python 3.12
- Conda
- Pip
- Git
```

### Installing

A step by step series of examples that tell you how to get a development env running

1. Clone the repository

```
git clone git@github.com:mukeshcodeshere/cgx_code.git
```

2. Navigate into the project directory

```
cd cgx_code
```

3. Create and activate a virtual conda environment

```
conda env create -f environment.yaml
conda activate cgx_code
```

4. Initialize the database with fake data (will become live data in future after API integration)

``` 
python db_init.py
```

5. Run the Flask application

```
python run.py
```

The app will now be running at `http://127.0.0.1:5000` (MIGHT BE DIFFERENT, LOOK AT BASH OUTPUT)