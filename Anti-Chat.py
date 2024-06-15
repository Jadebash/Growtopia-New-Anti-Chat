import time
import string
from collections import deque

class ChatMonitor:
    def __init__(self, base_block_duration=10, time_window=30):
        self.message_history = deque()  # Store tuples of (timestamp, words)
        self.blocked = False
        self.base_block_duration = base_block_duration
        self.current_block_duration = base_block_duration
        self.time_window = time_window
        self.username = None

    def normalize_message(self, message):
      
        return message.lower().translate(str.maketrans('', '', string.punctuation))

    def find_common_words(self, message):
        words = self.normalize_message(message).split()
        return words

    def send_message(self, message):
        current_time = time.time()
        
        if self.blocked:
            print("You are blocked from typing.")
            return
        
        normalized_words = self.find_common_words(message)
        self.message_history.append((current_time, normalized_words))
                                    
        while self.message_history and current_time - self.message_history[0][0] > self.time_window:
            self.message_history.popleft()

        if len(self.message_history) >= 3:
            word_count = {}
            for _, words in self.message_history:
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

            for word, count in word_count.items():
                if count >= 4:
                    self.blocked = True
                    print(f"You have been muted for {self.current_block_duration} seconds. Reason: Due to repeated word: {word}")
                    time.sleep(self.current_block_duration)  # Block the user for the specified duration
                    self.current_block_duration += self.base_block_duration  # Increase block duration
                    self.blocked = False
                    self.message_history.clear()  # Clear the history after blocking
                    print("You can type again.")
                    return
                  
        formatted_time = time.strftime("%H:%M:%S", time.localtime(current_time))
        print(f"[{formatted_time}] <{self.username}> {message}")

monitor = ChatMonitor()

username = input("Choose a username: ")
monitor.username = username

while True:
    message = input("Enter your message: ")
    monitor.send_message(message)
