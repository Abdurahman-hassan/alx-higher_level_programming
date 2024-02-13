#!/bin/bash
# the expand_aliases shell option is set using shopt -s expand_aliases.
shopt -s expand_aliases
alias cm='chmod u+x'
alias add='git add'
arg=$1
touch $arg
# add in the top of the file #!/usr/bin/node
echo '#!/usr/bin/node' > $arg
echo '' >> $arg
cm $arg
add $arg
