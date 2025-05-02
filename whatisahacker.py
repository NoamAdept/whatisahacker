#!/usr/bin/env python3
import base64, sys

# ── Configuration ─────────────────────────────────────────────────────────────
FLAG = "CTF{creativity-curiosity-collaboration}"
XOR_KEY = 0x42

# ── Helpers ────────────────────────────────────────────────────────────────────
def caesar(s: str, shift: int) -> str:
    out = []
    for c in s:
        if 'a' <= c <= 'z':
            out.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
        else:
            out.append(c)
    return "".join(out)

# ── Welcome ────────────────────────────────────────────────────────────────────
print("""
Welcome to the multilayer “What is a Hacker?” CTF!
Solve each layer in turn to reveal the final flag.
""".strip())
input("Press Enter to start Layer 1…")

# ── Layer 1: some sort of encoding  ─────────────────────────────────────────────────────────────
HINT1 = "U0hJRlQtNw==" 
print(f"\n[LAYER 1] Decode this Base64 block:")
print("  ", HINT1)
dec1 = base64.b64decode(HINT1).decode()
try:
    shift = int(dec1.split('-', 1)[1])
except Exception:
    print("\n⚠️  Failed to parse shift from Layer 1. Exiting.")
    sys.exit(1)

input("\nPress Enter for Layer 2…")

# ── Layer 2: some cipher ──────────────────────────────────────────────────────
L2 = "jylhapcpaf-jbypvzpaf-jvsshivyhapvu"
print(f"\n[LAYER 2] Decode this :")
print("  ", L2)
guess = input("\nEnter the decoded phrase (all lowercase, hyphens intact):\n> ").strip()
TARGET = "creativity-curiosity-collaboration"
if guess != TARGET:
    print("\n❌ Nope — that’s not it. Exiting.")
    sys.exit(1)

input("\n✔️  Correct! Press Enter for Layer 3…")

# ── Layer 3: some sort of encryption ─────────────────────────────────────────────────────
# Present the encrypted flag
HEX_FLAG = bytes([b ^ XOR_KEY for b in FLAG.encode()]).hex()
print(f"\n[LAYER 3] Here is the flag, XOR-encrypted and hex-encoded:")
print("  ", HEX_FLAG)

guess3 = input("\nEnter the decrypted flag string:\n> ").strip()
if guess3 == FLAG:
    print("\n🎉 Congratulations! Here is the flag:")
    print(f"    {FLAG}")
else:
    print("\n❌ Nope — that’s not it. Exiting.")
    sys.exit(1)

