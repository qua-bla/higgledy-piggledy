# applies many variables which should be allready set
set border linecolor rgb grid_hex 
set grid linecolor rgb grid_hex
set terminal epslatex size width cm , height cm color \
 header '\sansmath\sffamily\'.fontsize.'\newcommand{\cN}[1]{\color[rgb]{'.grid_dec.'}$\mathsf{#1}$}\newcommand{\cE}[1]{\cN{\num{#1}}}' fontspace
set grid
set format '\cN{%g}'

# default line width
default_line_width=4

set linetype 1 lw default_line_width
set linetype 2 lw default_line_width
set linetype 3 lw default_line_width
set linetype 4 lw default_line_width
set linetype 5 lw default_line_width
set linetype 6 lw default_line_width
set linetype 7 lw default_line_width
set linetype 8 lw default_line_width
set linetype 9 lw default_line_width
set linetype 10 lw default_line_width
set linetype 11 lw default_line_width
set linetype 12 lw default_line_width

# do not use yellow
set linetype 6 lc 7
set linetype 7 lc 8
set linetype 8 lc 9
set linetype 9 lc 10
set linetype 10 lc 11
set linetype 11 lc 12
set linetype 12 lc 13
