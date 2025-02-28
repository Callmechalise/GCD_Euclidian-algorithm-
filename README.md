# Finding GCD Using Euclidean Algorithm and Extended Euclidean Algorithm

This document explains two implementations of the **Euclidean Algorithm** for finding the **Greatest Common Divisor (GCD)**. It also covers the **Extended Euclidean Algorithm**, which finds integer coefficients satisfying **Bézout's Identity**.

## 📜 **History of the Euclidean Algorithm**
The **Euclidean Algorithm** was introduced by **Euclid** in his book *Elements* (~300 BC). It remains one of the oldest and most efficient methods to compute the GCD of two integers. The **Extended Euclidean Algorithm**, an enhancement of the original method, was later developed to express the GCD as a linear combination of the two numbers.

---

## 📌 **1. Euclidean Algorithm for GCD**
This method finds the GCD using repeated division.

### **🔹 Python Code:**
```python
# Finding GCD using Euclidean theorem
def gcd(r1, r2):
    print("Q  || r1   ||  r2   ||  r  ||")
    while r2 > 0:
        q = int(r1 / r2)  # Compute quotient
        r = r1 % r2       # Compute remainder
        print(f"{q}  ||  {r1}  ||  {r2}   ||  {r}  ||")
        r1 = r2  # Update r1 with r2
        r2 = r   # Update r2 with remainder
    print(f"\nGCD: {r1}\n")

if __name__ == "__main__":
    gcd(63, 84)
```

### ✅ **How it Works:**
1. Divide `r1` by `r2` and find the quotient `q` and remainder `r`.
2. Replace `r1` with `r2` and `r2` with `r`.
3. Repeat until `r2` becomes **0**.
4. The last nonzero remainder is the **GCD**.

#### **🛠 Example Execution:**
```
Q  || r1   ||  r2   ||  r  ||
1  ||  63  ||  84   ||  63  ||
1  ||  84  ||  63   ||  21  ||
3  ||  63  ||  21   ||  0  ||

GCD: 21
```
---

## 📌 **2. Extended Euclidean Algorithm**
This method finds the GCD and also computes integers `s` and `t` such that:
```
GCD(a, b) = s * a + t * b  (Bézout's Identity)
```

### **🔹 Python Code:**
```python
# Finding GCD using Extended Euclidean theorem
def gcd(r1, r2):
    print("Q  || r1   ||  r2   ||  r  ||  s1  ||  s2  ||  s  ||  t1  ||  t2  ||  t ||")
    s1, s2, t1, t2 = 1, 0, 0, 1
    while r2 > 0:
        q = int(r1 / r2)
        r = r1 % r2
        s = s1 - s2 * q
        t = t1 - t2 * q
        print(f"{q}  ||  {r1}  ||  {r2}   ||  {r}  ||  {s1}  ||  {s2}  ||  {s}  ||  {t1}  ||  {t2}  ||  {t}")
        r1, r2, s1, s2, t1, t2 = r2, r, s2, s, t2, t
    print(f"\nGCD: {r1}\n")
    print(f"s: {s1}\nt: {t1}")

if __name__ == "__main__":
    x = int(input("Enter greater number: "))
    y = int(input("Enter smaller number: "))
    gcd(x, y)
    print(f"GCD: {x} * s + {y} * t")
```

### ✅ **How it Works:**
1. It extends the Euclidean Algorithm by computing coefficients `s` and `t`.
2. These coefficients satisfy **Bézout's Identity**, which is useful in **modular inverses** and **Diophantine equations**.

#### **🛠 Example Execution:**
Input:
```
Enter greater number: 63
Enter smaller number: 84
```
Output:
```
Q  || r1   ||  r2   ||  r  ||  s1  ||  s2  ||  s  ||  t1  ||  t2  ||  t ||
1  ||  63  ||  84   ||  63  ||  1  ||  0  ||  1  ||  0  ||  1  ||  0  ||
1  ||  84  ||  63   ||  21  ||  0  ||  1  || -1  ||  1  ||  0  ||  1  ||
3  ||  63  ||  21   ||  0  ||  1  || -1  ||  0  ||  0  ||  1  || -3  ||

GCD: 21
s: 1
t: -1
Gcd:84s+63t
```

---

## 🔥 **Key Differences Between the Two Methods**
| Feature                     | Euclidean Algorithm | Extended Euclidean Algorithm |
|-----------------------------|---------------------|-----------------------------|
| **Finds GCD**               | ✅ Yes              | ✅ Yes                        |
| **Finds `s` and `t`**       | ❌ No               | ✅ Yes                        |
| **Used in cryptography**    | ❌ No               | ✅ Yes (RSA, modular inverse) |
| **Time Complexity**         | O(log N)           | O(log N)                     |

---

## 📌 **Conclusion**
- The **Euclidean Algorithm** is efficient for computing GCD.
- The **Extended Euclidean Algorithm** is essential for applications in **cryptography** and **number theory**.
- Both algorithms are widely used in **modular arithmetic** and **Diophantine equations**.

---

## 📌 **License**
This code is open-source. Feel free to use and modify it!

