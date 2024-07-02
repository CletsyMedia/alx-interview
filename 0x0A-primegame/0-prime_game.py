#!/usr/bin/python3

def isWinner(x, nums):
    def sieve(max_n):
        """ Return a boolean array is_prime where is_prime[i] is True if i is a prime number. """
        is_prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if (is_prime[p] == True):
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        return is_prime
    
    # Function to determine the winner of a single round
    def determine_round_winner(n):
        is_prime = sieve(n)
        prime_numbers = [i for i in range(n + 1) if is_prime[i]]
        
        maria_turn = True
        while True:
            if len(prime_numbers) == 0:
                return "Ben" if maria_turn else "Maria"
            
            # Maria's turn
            if maria_turn:
                pick = prime_numbers[0]
                prime_numbers = [num for num in prime_numbers if num % pick != 0]
            else:
                pick = min([num for num in range(1, n + 1) if is_prime[num]])
                if pick == float('inf'):
                    return "Maria"
                prime_numbers = [num for num in prime_numbers if num % pick != 0]
            
            maria_turn = not maria_turn
    
    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    # Iterate through each round
    for n in nums:
        winner = determine_round_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    # Example usage or testing code
    print(isWinner(5, [2, 5, 1, 4, 3]))

