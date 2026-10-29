# # 8-Bit Arithmetic and Logical Shift Operations Using Python

## 📌 Project Overview

This project demonstrates **8-bit arithmetic operations and logical shift operations using Python**. It explains how signed integers are represented using 8-bit two's complement representation and how binary numbers change during logical left and right shifts.

The project contains two programs:

1. **Program 1: 8-Bit Addition and Subtraction**
2. **Program 2: 8-Bit Logical Left and Right Shift**

## 🎯 Objectives

- Understand 8-bit binary representation.
- Perform addition and subtraction using two's complement.
- Convert decimal numbers into 8-bit binary.
- Detect carry-out and arithmetic overflow.
- Perform logical left and right shift operations.
- Display binary and decimal results.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Concepts:** Binary Arithmetic, Two's Complement, Bitwise Operations, Logical Shifting

## 📂 Project Structure

```text
8-bit-operations/
│
├── program1.py    # 8-bit addition and subtraction
├── program2.py    # Logical left and right shift operations
└── README.md      # Project documentation
```

## 🔢 Program 1: 8-Bit Addition and Subtraction

### Description

This program performs 8-bit addition and subtraction using two's complement representation.

It displays the binary representation of both operands, the result in binary and signed decimal, the carry-out bit, and the overflow status.

### Features

- Converts signed decimal numbers into 8-bit binary.
- Performs binary addition using a bit-by-bit full-adder process.
- Performs subtraction using two's complement.
- Calculates the carry-out bit.
- Detects signed arithmetic overflow.
- Converts the 8-bit result into signed decimal.

### Sample Operations

**Expression (a): 20 + 15**

```text
Operand A:  00010100 (+20)
Operand B:  00001111 (+15)
Carry-Out:  0
Result Bin: 00100011
Result Dec: 35
Overflow:   NO
```

**Expression (b): -20 + (-15)**

```text
Operand A:  11101100 (-20)
Operand B:  11110001 (-15)
Carry-Out:  1
Result Bin:  11011101
Result Dec:  -35
Overflow:   NO
```

### Key Concepts

- **Two's Complement:** Represents negative integers in binary.
- **Carry-Out:** Indicates a carry beyond the most significant bit.
- **Arithmetic Overflow:** Occurs when the mathematical result is outside the signed 8-bit range of -128 to +127.

## 🔄 Program 2: Logical Left and Right Shift

### Description

This program demonstrates logical left and right shifts on 8-bit binary numbers. Each shift moves the bits by one position, discards the bit that moves outside the 8-bit range, and fills the newly vacant position with zero.

### Features

- Converts integers into 8-bit binary strings.
- Performs logical left shifts.
- Performs logical right shifts.
- Displays each intermediate step.
- Shows the initial and final binary representations.
- Displays the unsigned decimal value after each shift.

### Sample Operations

**Logical Left Shift**

Initial binary: `10110110`

Number of positions: 2

```text
Step 1: 01101100
Step 2: 11011000

Final 8-bit Result: 11011000
Decimal Value: 216
```

**Logical Right Shift**

Initial binary: `11010100`

Number of positions: 2

```text
Step 1: 01101010
Step 2: 00110101

Final 8-bit Result: 00110101
Decimal Value: 53
```

### Key Concepts

- **Logical Left Shift (`<<`):** Moves bits to the left, discards the outgoing most significant bit, and appends zero at the right.
- **Logical Right Shift (`>>`):** Moves bits to the right, discards the outgoing least significant bit, and prepends zero at the left.
- **8-Bit Representation:** Maintains exactly eight binary digits.

## ▶️ How to Run the Programs

### Prerequisites

Install Python 3 on your computer.

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Open the Project Directory

```bash
cd 8-bit-operations
```

### Step 3: Run Program 1

```bash
python program1.py
```

### Step 4: Run Program 2

```bash
python program2.py
```

**Note:** Replace `<your-repository-url>` with your actual GitHub repository URL.

## 📚 Learning Outcomes

After completing this project, you will understand:

- How positive and negative numbers are represented using 8-bit two's complement.
- How binary addition and subtraction work at the bit level.
- The difference between carry-out and signed arithmetic overflow.
- How logical left and right shift operations work.
- How to implement low-level binary operations using Python.

## 🚀 Future Improvements

- Support user input for arithmetic operations.
- Add 8-bit multiplication and division.
- Demonstrate arithmetic right shift.
- Add automated test cases for different input values.
- Display detailed binary calculations for each operation.

## 👨‍💻 Author

**Yogeshwaran S.**

## 📄 License

This project is available for educational and learning purposes.
