# Growtopia-New-Anti-Chat

This Python code defines a ChatMonitor class that monitors chat messages for repeated use of specific words within a defined time window. Let's break down its functionality:

1. Imports and Initialization:

• import time: Imports the time module for timestamping and blocking functionality.

• import string: Imports the string module for punctuation removal.

• from collections import deque: Imports deque from the collections module to efficiently manage message history.

2. Class ChatMonitor:

• Attributes:

• message_history: A deque to store tuples of (timestamp, words) for recent chat messages.

• blocked: Indicates if the user is currently blocked from sending messages due to repeated words.

• base_block_duration: Initial duration in seconds for which a user is blocked.

• current_block_duration: Current duration in seconds a user remains blocked, which increases each time the user is blocked again.

• time_window: Time window in seconds within which repeated words are monitored.

• username: Stores the username of the chat participant.

• Methods:

• normalize_message(message): Converts the message to lowercase and removes punctuation using str.translate() and string.punctuation.

• find_common_words(message): Splits and normalizes a message into words after removing punctuation.

• send_message(message): Handles sending a message to the chat.

• Checks if the user is currently blocked. If so, prints a message and returns.

• Normalizes the message, appends it to message_history, and removes old messages outside time_window.

• If there are at least 3 messages in message_history, it counts the occurrences of each word.

• If any word appears 4 or more times, it blocks the user, prints a blocking message with the word causing the block, sleeps for current_block_duration seconds, increases current_block_duration, clears message_history, and unlocks the user after the block.

• Note: The send_message method also prints each message with a timestamp and the username.

3. Example Usage:

• Prompts the user to choose a username.

• Enters a loop where the user can continuously input messages.

• Each message input is passed to send_message, which processes and potentially blocks the user based on repeated word occurrences.

Summary: This ChatMonitor class effectively monitors chat messages, identifies repeated use of specific words within a defined time window, and applies increasing durations of blocking for users who violate the repetition threshold. It handles input/output, message normalization, and time-based operations to enforce chat rules.
