table.o: src/data/make_table.py src/data/*.csv
	python3 src/data/make_table.py

figure.o: src/data/*.gp src/data/*.csv
	cd ./src/data && ./*.gp && cd ../../

clean: template.tex
	latexmk -c
	rm -v *.aux *.fdb_latexmk *.fls

pdf: template.tex table.o figure.o
	latexmk -silent template.tex
	open template.pdf


.PHONY : run
