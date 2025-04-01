import hashlib

class Block:
    def __init__(self, number, transactions, previous_hash):
        self.number = number
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.secret_number = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.number}{self.transactions}{self.previous_hash}{self.secret_number}".encode()).hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != "0"*difficulty:
            self.secret_number += 1
            self.hash = self.calculate_hash()

class SimpleCoin:
    def __init__(self):
        self.blocks = []
        self.difficulty = 1
        self.pending = []
        self.reward = 10
        self.create_first_block()

    def create_first_block(self):
        first_block = Block(0, ["Создано 100 монет"], "0")
        first_block.mine(self.difficulty)
        self.blocks.append(first_block)

    def add_block(self, miner):
        new_block = Block(len(self.blocks), self.pending, self.blocks[-1].hash)
        new_block.mine(self.difficulty)
        self.blocks.append(new_block)
        self.pending = [f"Награда {self.reward} монет для {miner}"]

    def send_money(self, sender, receiver, amount):
        self.pending.append(f"{sender} -> {receiver}: {amount} монет")

    def show_blocks(self):
        for block in self.blocks:
            print(f"Блок #{block.number}:")
            print(f"Транзакции: {block.transactions}")
            print(f"Хеш: {block.hash[:10]}...")
            print()

# Играем с нашей криптовалютой
if __name__ == "__main__":
    print("🐉 Создаем DragonCoin - самую простую криптовалюту!")
    
    dragon_coin = SimpleCoin()
    
    print("💰 Первые транзакции:")
    dragon_coin.send_money("Аня", "Боря", 5)
    dragon_coin.send_money("Боря", "Ваня", 3)
    
    print("⛏️ Майним блок (добываем новые монеты)...")
    dragon_coin.add_block("Майнер Петя")
    
    print("💸 Еще транзакции:")
    dragon_coin.send_money("Ваня", "Аня", 2)
    dragon_coin.send_money("Майнер Петя", "Боря", 1)
    
    print("⛏️ Майним еще один блок...")
    dragon_coin.add_block("Майнер Маша")
    
    print("\n📦 Вот так выглядит наш блокчейн:")
    dragon_coin.show_blocks()
    
    print("🎉 Ура! Мы создали свою криптовалюту!")
