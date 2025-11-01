# 🌱 SeedStorm

### 🧩 Description  
SeedStorm is a Python project that creates random numbers using unique seed values.  
It never repeats a number unless asked. Each number and its seed are saved in a text file, allowing you to search by seed later.  

This project is a fun and simple way to understand how randomness works in Python — and how seeds, loops, and files can work together.  

---

### 🧠 Code Explanation (Line by Line)

```python
import random
import time
import os
```
These lines import Python modules:
- **random** → for generating random numbers.  
- **time** → for adding small delays or tracking time between generations.  
- **os** → for handling file operations like checking or creating files.

---

```python
a = 0
for x in range(5):
    while True:
        seed_number = random.randint(99, 9999999)
```
- `a = 0` sets an initial counter variable.  
- `for x in range(5):` runs the main loop 5 times (you can change this number).  
- Inside it, `while True:` creates an infinite loop that keeps generating numbers.  
- `seed_number = random.randint(99, 9999999)` picks a random seed value between 99 and 9,999,999.

---

```python
        random.seed(seed_number)
        randd = random.randrange(999, 9999999)
```
- `random.seed(seed_number)` tells Python to use that seed to generate a number.  
- `randd = random.randrange(999, 9999999)` creates the random number itself.  
Every seed creates a unique pattern of numbers — so the same seed always gives the same result.

---

```python
        with open("seed_data.txt", "a") as file:
            file.write(f"{seed_number} : {randd}\n")
```
- This part opens (or creates) a text file named **seed_data.txt**.  
- It adds each new pair of seed and random number to the file — one per line.  
- Example line in the file:  
  ```
  472193 : 5812394
  ```

---

```python
        print(f"Seed: {seed_number} | Number: {randd}")
```
- Prints the result on the screen so you can see what’s happening live.

---

```python
        time.sleep(1)
```
- Adds a one-second pause before the next number — this helps you observe the process slowly and clearly.

---

### 🔧 Features
- Generates random numbers using unique seeds  
- Never repeats numbers unless you ask for it  
- Saves all outputs in a text file for record keeping  
- Lets you search for numbers by their seed  
- Great for learning randomness, loops, and file handling  

---

### 📂 Example Output in `seed_data.txt`
```
1573 : 5938472
4984 : 2389405
7852 : 9912741
```

---

### 🚀 How to Run
1. Save the code as `seedstorm.py`.  
2. Run it in your terminal or VS Code using:  
   ```bash
   python seedstorm.py
   ```  
3. Check the generated file `seed_data.txt` to see all results.  

---

### 🧠 Learnings
- How `random.seed()` works  
- How loops generate continuous output  
- How to write and store data in files  
- How to control and track random generation  

---

### 📜 License
This project is open-source and free for educational use.

**Created by:** Vibek 
**Language:** Python  
**Version:** 1.0
