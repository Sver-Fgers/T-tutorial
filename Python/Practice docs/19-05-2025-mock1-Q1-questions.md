# Sequences & Mathematical Computations)

- instructions
	- after opening the file, go to community plugins and install the plugin `Latex suites`
	- enable it and the contents will render properly
	- after you are done with solving on vscode, rename the file as `19-05-2025-mock1-Q1-answers`
	- add it to the root folder inside obsidian (that means don't put it inside any folder, just leave it in the default home directory).
	- the question are on sums, products, trigonometric functions, logarithms, combinatorics and programming (input validation, math operations and complexity analysis).
## Question 1  
We define $T_n$ for $n \in \mathbb{N}$ as:  
$$ T_n = \sum_{k=1}^{n} \frac{k^3 + 2k}{3} $$  

**Tasks:**  
1. Write a program that reads an integer $n$ from standard input and calculates $T_n$  
2. Check if the input is a positive integer (print error if invalid)  
3. State and justify the time complexity of your solution  

---

## Question 2  
Define $U_n$ as:  
$$ U_n = \prod_{k=1}^{n} \left(1 + \frac{1}{k^2}\right) $$  

**Tasks:**  
1. Write a function `calculate_U(n)` that computes $U_n$ for a given $n$ 
2. Handle the case $n = 0$ by returning 1.
3. what is the runtime complexity of your program. justify your answer clearly
---

## Question 3  
For $n \in \mathbb{N}$:  
$$ V_n = \sum_{k=1}^{n} \frac{(-1)^k \cdot k}{k + 1} $$  

**Tasks:**  
1. Write a program to compute $V_n$  
2. Print intermediate results for each term $k$ (e.g., "k=1:-0.5") 
3. what is the runtime complexity of your program. justify your answer clearly

---

## Question 4  
Given the sequence:  
$$ W_n = \sum_{k=1}^{n} \frac{2^k + k}{k!} $$  

**Tasks:**  
1. Implement a function `compute_W(n)` to calculate $W_n$  
2. Compare the result with $e^2$ (use `math.exp(2).` print the absolute difference) 
3. what is the runtime complexity of your program. justify your answer clearly
---

## Question 5  
Define $X_n$ as:  
$$ X_n = \sum_{k=1}^{n} \frac{\ln(k + 1)}{k} $$  

**Tasks:**  
1. Write a program to compute $X_n$ using natural logarithm `math.log`
2. what is the runtime complexity of your program. justify your answer clearly

---

## Question 6  
For $n \in \mathbb{N}$, let:  
$$ Y_n = \sum_{k=1}^{n} \sin\left(\frac{k\pi}{4}\right) $$  

**Tasks:**  
1. Calculate $Y_n$  and print the result
2. Validate input to ensure $n$ is a non-negative integer.

---

## Question 7  
Define $Z_{n}$ as:  
$$ Z_n = \sum_{k=1}^{n} \frac{k^2 \cdot \cos(k)}{2^k} $$  

**Tasks:**  
1. Implement a function `calculate_Z(n)` to compute $Z_n$
2. Print result with 4 decimal places  
3. what is the runtime complexity of your program. justify your answer clearly

---

## Question 8  
Given:  
$$ A_n = \sum_{k=1}^{n} \frac{1}{k^2 + k} $$  

**Tasks:**  
1. Compute $A_n$ and verify that $A_n = 1 - \frac{1}{n + 1}$  
2. what is the runtime complexity of your program. justify your answer clearly

---

## Question 9  
For $n \in \mathbb{N}$:  
$$ B_n = \sum_{k=1}^{n} \binom{n}{k} \cdot \frac{1}{2^k} $$  

**Tasks:**  
1. Compute $B_n$ using combinations  `math.comb`
2. Compare the result with $\left(\frac{3}{2}\right)^n - 1$  
3. what is the runtime complexity of your program. justify your answer clearly

---

## Question 10  
Let $C_{n}$ be:  
$$ C_n = \sum_{k=1}^{n} \frac{F_k}{k} $$  
where $F_k$ is the $k$-th Fibonacci number.  
1. Write a program to compute $C_{n}$
2. what is the runtime complexity of your program. justify your answer clearly

---

