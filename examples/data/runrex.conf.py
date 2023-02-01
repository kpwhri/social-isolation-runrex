from pathlib import Path

path = Path(r'examples/data')
config = {
    'corpus': {
        'directory': str(path / 'corpus'),
        'connections': [
            {
                'name': str(path / 'corpus.csv'),
                'name_col': 'doc_id',
                'text_col': 'text',
            }
        ]
    },
    'output': {
        'name': 'social_isolation_runrex_results_{datetime}',
        'kind': 'jsonl',
        'path': str(path / 'out')
    },
}
print(config)
