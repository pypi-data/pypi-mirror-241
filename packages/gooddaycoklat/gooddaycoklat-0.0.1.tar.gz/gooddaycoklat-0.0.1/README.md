# Foobar

MyGeometry adalah paket Python sederhana yang berisi modul untuk menghitung luas bentuk geometris.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install mygeometry
```

## Usage

from mygeometry.shapes.trapesium import Trapesium

#Membuat objek Trapesium
trapesium_saya = Trapesium(alas=5, atas=7, tinggi=4)

#Menghitung dan menampilkan luas trapesium
print(f"Luas trapesium: {trapesium_saya.luas()}")