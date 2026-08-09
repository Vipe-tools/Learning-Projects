S = " "
T = "\t"
L = "\n"


def push(n):
    bits = bin(n)[2:]
    return S + S + S + "".join(T if b == "1" else S for b in bits) + L


def print_char():
    return T + L + S + S


program = ""

for char in "Hello World!":
    name = "SPACE" if char == " " else char

    program += f"[PUSH_{name}_{ord(char)}]"
    program += push(ord(char))

    program += f"[PRINT_{name}]"
    program += print_char()

program += "[END]"
program += L + L + L

with open("helloworld.ws", "w", newline="") as f:
    f.write(program)

print("helloworld.ws successfully created.")
