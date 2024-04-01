# Curiosity Global Exchange  
## Improving Liquidity between FICC instruments & Cryptocurrencies

### Clone the repo
1) git clone git@github.com:mukeshcodeshere/cgx_code.git
2) cd cgx_code

### Create and Activate environment 
3) conda env create -f environment.yaml
4) conda activate cgx_code

### Run the script to initialize the database [FAKE DATA] 
### TODO:Need to integrate live data from APIs
5) python db_init.py

### Run Flask application
6) python run.py