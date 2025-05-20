To test the system
Please run the following command in terminal (this is the command for iOS, Windows may have smalll difference):


mkdir banking_system

cd banking_system

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python -m pytest tests/ -v

python main.py

