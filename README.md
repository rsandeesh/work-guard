# Install packages
pip3 install -r requirements.txt

# Run app
## Export variables
export DBUSER='postgres'
export DBPASS=
export DBHOST='localhost:5432'
export DATABASE='work_guard'
export DBPARAMS=
export VERBOSE='True'
export APP_DEBUG='True'
export ENV='development'

functions-framework-python --target chat


# Deploy
gcloud functions deploy kaya-aia-general-bot  --region=us-central1 --source=./ --runtime=python310 --trigger-http --env-vars-file .env.dev.yaml --entry-point=chat

# Run
uvicorn main:app --host 0.0.0.0 --port 8080 --reload

python3 -m uvicorn main:app --host 0.0.0.0 --port 8080 --reload

# Add content the requirements.txt
pipreqs . --force
pip freeze > requirements.txt

# Formatting

https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8

# Setting up virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Running scripts
python -m resources.scripts.pg_convert
python -m resources.scripts.user_migration_script

# Library Imports
- Standard library imports
- Related third-party imports
- Local application/library specific imports
