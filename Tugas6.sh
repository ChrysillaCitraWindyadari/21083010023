#!/bin/bash

#deklarasi array
declare -a arrIPS

#user input jumlah element dalam array
echo -n "Input : "
read n

#user input nilai-nilai di dalam array
for ((i=0; i<n; i=i+1))
do
  read arrIPS[$i]
done

#perhitungan nilai IPK
sumIPS=0;
for i in ${arrIPS[@]};
do
  let sumIPS+=$i;
  let hasil=$sumIPS/$n;
done

#print out
echo ""
echo -e "IPS mhs = $sumIPS / $n"
echo -e "IPK mhs = $hasil"


