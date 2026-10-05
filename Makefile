up:
	docker compose up --build research
notebook:
	docker compose up --build notebook
paper:
	docker compose run --rm paper
test:
	pytest -q
bench:
	python benchmarks/benchmark_suite.py
all:
	python experiments/run_all.py && pytest -q && python benchmarks/benchmark_suite.py
