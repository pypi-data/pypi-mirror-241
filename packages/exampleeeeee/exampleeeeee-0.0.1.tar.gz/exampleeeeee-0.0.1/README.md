# ci_cd_example

1) create repository
2) write example/main.py (add documentation)
add setup.py, requirements.txt
3) docs
- create .readthedocs.yml, docs/, docs/conf.py, docs/source/index and docs/source/api/linear_equation
- publish to readthedocs
4) test
- create test/, test/test_scripts/, write test_linear_equation, and write run_all_tests.py
5) continuous integration (circleci)
https://app.circleci.com/projects/setup/
set up .circleci, .circle/config.yml
6) pypi
python setup.py sdist bdist_wheel
twine upload --repository pypi dist/* -u $PYPI_USERNAME -p $PYPI_PASSWORD
__token__

7) tag