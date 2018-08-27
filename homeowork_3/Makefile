cover:
	make lint
	make cover_tests

lint:
	flake8 --max-line-length=100 algos tests

cover_tests:
	py.test -s  --cov-config .coveragerc --cov algos \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	tests
