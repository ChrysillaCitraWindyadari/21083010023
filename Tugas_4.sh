#!/bin/bash

echo -n "Input acuan bilangan : ";
read a

if [ `expr $a % 2` -eq 1 ]
then
  while [[ $a -ge 1 ]]
  do
    echo $a
    a=$((a - 2))
  done
else
  echo "Input acuan bilangan ganjil"

fi
