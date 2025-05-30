python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cd tusi-web
python manage.py runserver
