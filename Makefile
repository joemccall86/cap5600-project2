DOT=dot
PANDOC=pandoc

all: report.pdf

%.pdf: %.md *.bib
	$(PANDOC) -N --filter pandoc-crossref --filter pandoc-citeproc -o $@ $<

clean:
	rm -f report.pdf
