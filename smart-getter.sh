#!/bin/bash

html=$(<index-master.html)
details=`snapraid smart -v`

# Replace 60% 70% 80% 90% with tet \1
echo $details | sed -E 's|([6789]0\%)|tet \1|'

printf "$html" "$details" > index.html


# for drive in /dev/sd[a-z]
# do
#     disk=$(sed "s|/dev/||g" <<< $drive)
#     label=$(blkid -s LABEL | grep $disk | sed -r 's|^.*"(.*)"|\1|')

#     smartctl -a $drive -d sat > "drive/$disk ($label)"
# done
