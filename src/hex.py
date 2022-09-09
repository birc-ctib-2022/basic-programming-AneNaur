import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        encoding = "".join(hex(ord(c)) for c in x)
        print(encoding)

    case "decode":
#        number=encoding.split("0x") #Når vi splitter, får man alt på venstre side af det vi splitter efter, så hvis "encoding" starter med "0x" får vi en tom streng som vores første plads i "number".
        decoding = "".join([chr(int(n, base=16)) for n in x.split("0x")[1:]])
        print(decoding)
