### bq_lookml_generator v.0.1.1

This automatic generator is buit over Josh Temples looker parser [https://github.com/joshtemple/lkml]. Building out lkml, it allows you to generate lookml from BigQuery metadata. 

## Getting started

- make sure you are working in a venv.
- head to /lookml/bq_lookml_gen
- set up your bq_lookml_gen service account
- input your secrect path in here lookml/bq_lookml_gen/config.py

        service_account = service_account.Credentials.from_service_account_file(
            ['path_to_file.json'],
        )
- input your warehouse schema target in here lookml/bq_lookml_gen/warehouse_target.py
- type bq_lookml_gen into terminal and watch the base explore generate... 

## troubleshooting 

- run pip install -r requirements.txt if you are running into dependency issues
- you can run bq_lookml_gen.py from terminal if needed


