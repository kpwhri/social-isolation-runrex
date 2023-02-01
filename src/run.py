from runrex.main import process
from runrex.text.ssplit import regex_ssplit
from runrex.util import algo_to_result
from runrex.schema import validate_config

from social_isolation.algo.alone import is_alone
from social_isolation.algo.isolation import has_social_isolation


def main(config_file):
    conf = validate_config(config_file)
    algorithms = {
        'isolation': lambda d, e: algo_to_result(has_social_isolation, d, e),
        'alone': lambda d, e: algo_to_result(is_alone, d, e),
    }
    process(**conf, algorithms=algorithms, ssplit=regex_ssplit)


if __name__ == '__main__':
    import sys

    try:
        main(sys.argv[1])
    except IndexError:
        raise AttributeError('Missing configuration file: Usage: run.py file.(json|yaml|py)')
