# Steps

In these cases, you may need to update the appropriate paths.

## Step 1: Run Regex

* Create your own version of `runrex.conf.py` to ensure that paths correctly line up
* `python src\run.py examples\data\runrex.conf.py`


## Step 2: Organize Outputs

* `python src\extract_and_load_json.py --file examples\data\out\social_isolation_runrex_results_DATE --version runrex`


## Step 3: Build Variables

* `python src\build_variables.py --file examples\data\out\social_isolation_runrex_results_DATE.csv --metafile examples\data\metadata.csv`

