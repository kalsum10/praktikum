## Cara kerja program
Ketika program dijalankan, maka program akan menampilkan output "Masukkan nomor telepon (atau ketik 'selesai' jika sudah selesai):" ketika kita sudah menginputkan nomor telpon dan nama maka kita ketikan selesai. Setelah kita mengetikan selesai maka akan menampilkan histori dari telpon tersebut
Dan untuk elemen penting dari program ini yaitu 
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

telepon = LinkedList()
while True:
    nomor_telepon = input("Masukkan nomor telepon (atau ketik 'selesai' jika sudah selesai): ")
    if nomor_telepon.lower() == "selesai":
        break
    telepon.add(nomor_telepon)

# Tampilkan histori telepon
telepon.display()

# fungsionalitas 
Singly linked list adalah sebuah Linked list yang menggunakan sebuah variabel pointer saja untuk menyimpan banyak data dengan metode linked list, suatu daftar isi yang saling berhubungan sehingga akan membuat sekumpulan dari node yang saling terhubung dengan node lain melalui sebuah pointer.
