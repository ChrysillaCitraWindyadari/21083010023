#!/bin/bash
clear
 
echo "Tugas 2 Percabangan Sederhana Aritmatika"
echo "Nama : Chrysilla Citra Windyadari"
echo "NPM  : 21083010023"
echo "-----------------------------------------------------"
echo "Operasi aritmatika :"
echo "1. Penjumlahan"
echo "2. Pengurangan"
echo "3. Perkalian"
echo "4. Pembagian"
echo "5. Modulus"
echo "6. Perbandingan nilai"
echo "-----------------------------------------------------" 
echo -n "Masukkan nilai a: ";
read a;
echo -n "Masukkan nilai b: ";
read b;
echo -n "Masukkan nomer operasi aritmatika : ";
read aritmatika;

if [ $aritmatika == "1" ]
  then
  plus=$(( $a + $b ))
  echo "Hasil penjumlahan a dan b adalah $plus"
elif [ $aritmatika == "2" ]
  then
  minus=$(( $a - $b ))
  echo "Hasil pengurangan a dan b adalah $minus"
elif [ $aritmatika == "3" ]
  then
  let multiple=$a*$b
  echo "Hasil perkalian a dan b adalah $multiple" 
elif [ $aritmatika == "4" ]
  then
  let divide=$a/$b
  echo "Hasil pembagian a dan b adalah $divide"
elif [ $aritmatika == "5" ]
  then
  module=`expr $a % $b`
  echo "Hasil modulus a dan b adalah $module"
elif [ $aritmatika == "6" ]
 then
  if [ $a == $b ]
  then 
    echo "a and b have same value"
  elif [ $a != $b ]
  then
    echo "a and b have different value"
  else
    echo "Error"
  fi
else
  echo "Sorry command can't execute"
fi
