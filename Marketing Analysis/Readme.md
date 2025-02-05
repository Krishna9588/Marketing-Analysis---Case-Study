# Marketing Analysis


### Technologies Used
- Python -- 13.2.7
- Pandas Lib -- 2.2.3


#### Clone this Repository
```bash
    git clone https://github.com/Krishna9588/Marketing-Analysis---Case-Study-.git
```

#### Installation
```bash
    pip install -r requirements.txt
```
Then Run [check](check.py) file to verify if pandas is installed or not


#### Run Project 
```bash
    python main.py
```
Else go to [main.py](main.py) and click Run.


#### Dataset
In Dataset folder we have 
[Customer information](dataset/purchase_behaviour.csv)
and 
[Transaction Details](dataset/transaction_data.csv)

---
### Code Explanation & working

#### 1. [Operations](operations.py)
* .read_csv - to access the information of dataset
* .merge() - to merge the data from both the file using Primary and Foreign key (**LYLTY_CARD_NBR**)

#### 2. [Best Sellers](bestSellers.py)
* .group_by - to make bring similar product together
* .sum() - total of all similar products
* .sort_values() - to arrange product from high to low

#### 3. [Loyal Customer](loyal_Customers.py)
* .value_count() - to get discrete values only  
* .quantile(x) - to get values above x percentage 
* .agg() - to use multiple operations together
 
---

### [Output](output.txt)

This file has output structure which we can expect after running the program successfully

---
