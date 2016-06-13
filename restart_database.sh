#!/bin/bash

rm -rf db_repository
rm -rf app.db
rm -rf tmp
rm -rf templates/*

python db_create.py
python db_migrate.py
python run.py
