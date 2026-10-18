# Fibonacci Pattern Generator

A simple Python script that prints the Fibonacci sequence up to the number of terms you choose.

## What is the Fibonacci sequence?

The Fibonacci sequence is a series of numbers where each number is the sum of the two before it:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

## Requirements

- Python 3.x
- No external libraries needed

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Run the script:
   ```bash
   python fibonacci.py
   ```

3. Enter how many Fibonacci numbers you want when prompted:
   ```
   [INPUT] How many numbers of the Fibonacci pattern do you want :10
   ```

## Example Output

Input: `10`

```
0,1,1,2,3,5,8,13,21,34,
```

## How It Works

1. The script starts with two variables, `number1` and `number2`, both set to `1`.
2. It prints the first three numbers of the sequence (`0,1,1`) directly.
3. A loop runs `pattern_number - 3` times. In each step it:
   - adds `number1` and `number2` to get the next number,
   - prints that number,
   - shifts the values forward (`number1` takes `number2`'s value, `number2` takes the new number).

## Code

```python
number1 = 1
number2 = 1
number = 0
pattern_number = int(input("[INPUT] How many numbers of the Fibonacci pattern do you want :"))

print("0,1,1", end=",")
for i in range(pattern_number - 3):
    number = number1 + number2
    print(number, end=",")
    number1 = number2
    number2 = number
```

## Known Limitations

- The first three numbers (`0,1,1`) are always printed, even if you enter a number smaller than 3.
- The output ends with a trailing comma.
- Entering a non-number (like text) will cause an error.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
