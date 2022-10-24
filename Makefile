#Database
migrations:
	python ./advanced_orm/manage.py makemigrations

migrate:
	python ./advanced_orm/manage.py migrate

drop_migrations:
	python ./advanced_orm/manage.py migrate shop zero

init_db:
	python ./advanced_orm/manage.py init_demo_db

clean_db:
	python ./advanced_orm/manage.py clean_up_demo_db

refill_db: clean_db init_db
