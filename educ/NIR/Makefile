all: build

build:
	latexmk -xelatex -synctex=1 main.tex

run: build clean
	# Я использую xreader для просмотра PDF
	xreader presentation.pdf &

clean:
	rm *.aux \
	*.fdb_latexmk \
	*.fls \
	*.log \
	*.out \
	*.synctex.gz \
	*.toc \
	*.snm \
	*.nav
