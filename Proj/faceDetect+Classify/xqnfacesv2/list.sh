#!/bin/bash
echo "this script is to rename picture"

for names in $(ls $PWD)
do
    echo $names>>list
done

