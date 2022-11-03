1. Set up python environment
2. Install packages
```sh
pip install -r requirements.txt
```
3. Create migrations
```sh
python manage.py makemigrations
```
4. Apply migrations
```sh
python manage.py migrate
```
5. Create superuser
```sh
python manage.py createsuperuser
```
6. Run server
```sh
python manage.py runserver
```
| Info | URL |
| ------ | ------ |
| Login Page | http://127.0.0.1:8000/login/ |
| Page for uploading new users (need admin permission) | http://127.0.0.1:8000/ |
| User logged-in home page | http://127.0.0.1:8000/home |

