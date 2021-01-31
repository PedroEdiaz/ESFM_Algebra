touch output.tex

python3 main.py | tee -a output.tex

sed -i '/^\t[0-9])/d' output.tex
sed -i '/^[a-z]/d' output.tex
sed -i '/^De/d' output.tex
sed -i '/^Programa/d' output.tex
sed -i '/^>/d' output.tex
