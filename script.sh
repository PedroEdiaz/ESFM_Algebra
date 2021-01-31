cp ~/Plantillas/skeleton.tex output.tex

sed -i '/\end{document}/d' output.tex

python3 main.py | tee -a output.tex

sed -i '/^\t[0-9])/d' output.tex
sed -i '/^[a-z]/d' output.tex
sed -i '/^De/d' output.tex
sed -i '/^Programa/d' output.tex
sed -i '/^>/d' output.tex

echo '\n\\end{document}' >> output.tex

pdflatex output.tex >> /dev/null
rm *.aux *.log
xdg-open output.pdf 
