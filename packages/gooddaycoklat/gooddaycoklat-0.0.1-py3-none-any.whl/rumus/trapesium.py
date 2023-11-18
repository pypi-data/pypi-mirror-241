# trapesium.py

class Trapesium:
    def __init__(self, alas, atas, tinggi):
        """
        Inisialisasi objek Trapesium.

        Parameters:
        - alas (float): Panjang alas trapesium.
        - atas (float): Panjang atas trapesium.
        - tinggi (float): Tinggi trapesium.
        """
        self.alas = alas
        self.atas = atas
        self.tinggi = tinggi

    def luas(self):
        """
        Menghitung luas trapesium.

        Returns:
        float: Luas trapesium.
        """
        return 0.5 * (self.alas + self.atas) * self.tinggi

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek Trapesium
    trapesium_saya = Trapesium(alas=5, atas=7, tinggi=4)

    # Menghitung dan menampilkan luas trapesium
    print(f"Luas trapesium: {trapesium_saya.luas()}")
