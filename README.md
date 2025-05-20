To test the system
Please run the following command in terminal (this is the command for iOS, Windows may have smalll difference):


mkdir banking_system

cd banking_system

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python -m pytest tests/ -v

python main.py



Note: the banking_system folder contain the runing results, it should not influence your running but if you want to run from scratch, please delete _pycache_ folder and accounts.csv.
