build:
	@docker build -t pdf-interpreter .
run:
	@docker run --rm pdf-interpreter
exec:
	@docker run --rm pdf-interpreter pdf2txt.py ejemplo-bbva.pdf
