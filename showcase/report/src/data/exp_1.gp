#!/opt/homebrew/bin/gnuplot

set term tikz
set output "showcase.tex"
set size square
set xlabel "時間$t$ / s	"
set ylabel "水温$T$ / \\si{\\celsius}"
f(t) = a*t + b
fit f(x) "e_showcase.csv" via a, b
plot [t=0:] "e_showcase.csv" notitle, f(t)
