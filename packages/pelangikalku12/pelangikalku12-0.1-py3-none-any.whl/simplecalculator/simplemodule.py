class SimpleCalculator:
    def add(self, a, b):
        """Tambahkan dua angka."""
        return a + b

    def subtract(self, a, b):
        """Kurangkan dua angka."""
        return a - b

    def multiply(self, a, b):
        """Kalikan dua angka."""
        return a * b

    def divide(self, a, b):
        """Bagikan dua angka."""
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol.")
        return a / b
