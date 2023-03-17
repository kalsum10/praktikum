class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("Histori telepon kosong.")
        else:
            current = self.head
            print("Histori telepon:")
            while current is not None:
                print(current.data)
                current = current.next

# Contoh penggunaan
telepon = LinkedList()

# Loop untuk meminta input nomor telepon
while True:
    nomor_telepon = input("Masukkan nomor telepon (atau ketik 'selesai' jika sudah selesai): ")
    if nomor_telepon.lower() == "selesai":
        break
    telepon.add(nomor_telepon)

# Tampilkan histori telepon
telepon.display()
