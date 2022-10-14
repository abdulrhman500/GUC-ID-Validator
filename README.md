# GUC_ID_Validator
 Simple API using Django done as a task to join IEEE club at the GUC

## How to install
```bash
git clone 
python -m venv .venv
. .venv\Scripts\activate
pip install django
```
## How to use
```bash
cd IEEE_Tasks/Tasks
python manage.py runserver
``` 
Then open
```bash
http://127.0.0.1:8000/[ID] #write the id number without the brackets
```
## Example 

#### Input
```bash
http://127.0.0.1:8000/52-1234
```
####  Output
```
Valid ID  
Entrance Year: 2020
```

####  Input
```bash
http://127.0.0.1:8000/51-1234
```
#### Output
```
NOT A VALID ID.
```
