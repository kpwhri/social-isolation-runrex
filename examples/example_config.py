"""
Example configuration file using SQL Server.
"""
import os

path = r'WORKING_DIR_FOR_LOGS_AND_OUTPUT'
config = {
    'corpus': {
        'connections': [
            {
                'name': 'social_isolation_notes',
                'driver': 'SQL Server',
                'server': 'SQL_SERVER_SERVER_NAME',
                'database': 'SQL_SERVER_DATABASE_NAME',
                'name_col': 'NOTEID',
                'text_col': 'NOTETEXT',
            }
        ],
    },
    'output': {
        'name': 'social_isolation_runrex_results_{datetime}',
        'kind': 'jsonl',
        'path': os.path.join(path, 'out')
    },
    'select': {  # comment this out if you want to run on larger sample
        'start': 0,
        'end': 1000,
    },
    'loginfo': {
        'directory': os.path.join(path, 'log')
    },
}
print(config)
