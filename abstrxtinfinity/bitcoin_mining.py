from hashlib import new, sha256
import time

MAX_NONCE = 100000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros

    for nonce in range(MAX_NONCE):
        nonce += 1
        text = str(block_number) + transactions + prev_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"\nYay!! Successfully mined bitcoins with nonce value:{nonce} ")
            return new_hash

    raise BaseException(f"Couldn't findcorrect Hash after trying {MAX_NONCE} times")


if __name__ == "__main__":
    transactions = """
    Rohan->Mohan->20,
    Chandan->Chaman->45
    """
    prev_hash = "0000000xa036944e29568a66bd0cff17edbe0381544208feacf9a66b65as68wqe4551vvfb54gf1set70der58feacf965as645asd5et"

    difficulty = 10

    start = time.time()  ##?Gives Current Time
    print("\nMining Started")
    new_hash = mine(5, transactions, prev_hash, difficulty)
    total_time = str(time.time() - start)
    print(f"\nMining Ends. Time Taken = {total_time} seconds")

    print("\n")
    print(new_hash)
    print("\n")
