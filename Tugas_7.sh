#!/bin/bash

# Mendeklarasikan fungsi
function panjang {
    echo "Masukkan Panjang : "
    read panjang
}
function lebar {
    echo "Masukkan Lebar : "
    read lebar
}
function luas {
     let luas=$panjang*$lebar
     echo -e "Luas Persegi : \n$luas"
}

# Memanggil fungsi
panjang
lebar
luas

