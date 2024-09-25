import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):  # Perbaiki _init_ menjadi __init__
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Menghitung hash dari blok berdasarkan atribut-atribut blok tersebut.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()  # Perbaiki cha256 menjadi sha256 dan ancode menjadi encode

    def __repr__(self):  # Perbaiki repr menjadi __repr__
        return (f"Block(index: {self.index}, hash: {self.hash}, Previous_hash: {self.previous_hash}, "
                f"timestamp: {self.timestamp}, data: {self.data}, nonce: {self.nonce})")

class Blockchain:
    def __init__(self):  # Perbaiki _init_ menjadi __init__
        self.chain = [self.create_genesis_block()]  # Perbaiki {} menjadi ()
        self.difficulty = 4  # Perbaiki = menjadi =

    def create_genesis_block(self):
        """
        Blok pertama dalam blockchain, disebut sebagai blok genesis.
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        """
        Mengembalikan blok terakhir di dalam blockchain
        """
        return self.chain[-1]

    def add_block(self, new_block):  # Perbaiki penempatan metode
        """
        Menambahkan blok baru ke dalam blockchain setelah memvalidasi proof of work.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block):
        """
        Proses penambangan sederhana yang mencoba menemukan hash yang valid (dengan kesulitan tertentu).
        """
        block.nonce = 0
        calculated_hash = block.calculate_hash()
        while not calculated_hash.startswith('0' * self.difficulty):  # Perbaiki whole menjadi while
            block.nonce += 1
            calculated_hash = block.calculate_hash()  # Perbaiki calculated.hash menjadi calculated_hash
        return calculated_hash

    def is_chain_valid(self):
        """
        Memeriksa validitas blockchain dengan memverifikasi setiap blok dan hash yang saling merujuk.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]  # Perbaiki sellf menjadi self
            previous_block = self.chain[i - 1]

            # Periksa apakah hash blok saat ini benar
            if current_block.hash != current_block.calculate_hash():
                print(f"Hash of block {i} is invalid!")
                return False
            
            # Periksa apakah blok ini merujuk ke hash blok sebelumnya dengan benar
            if current_block.previous_hash != previous_block.hash:
                print(f"Previous hash of block {i} is invalid!")
                return False
        
        return True

# Demonstrasi

# Membuat blockchain baru
my_blockchain = Blockchain()

# Menambah beberapa blok baru ke dalam blockchain
my_blockchain.add_block(Block(1, "", time.time(), "Transaksi 1"))  # Perbaiki add_bloock menjadi add_block
my_blockchain.add_block(Block(2, "", time.time(), "Transaksi 2"))  # Perbaiki add_bloock menjadi add_block
my_blockchain.add_block(Block(3, "", time.time(), "Transaksi 3"))  # Perbaiki add_bloock menjadi add_block

# Cetak seluruh blok di dalam blockchain
for block in my_blockchain.chain:
    print(block)

# Memeriksa apakah blockchain valid
print(f"Apakah blockchain valid? {my_blockchain.is_chain_valid()}")  # Perbaiki Print menjadi print
