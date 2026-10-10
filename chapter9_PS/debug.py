# debug_rehan_file.py
import os, sys

fname = "rehan.txt"
print("Current Working Directory:", os.getcwd())
full = os.path.abspath(fname)
print("Trying file:", full)
print("Exists:", os.path.exists(full))
print("Files in folder:", os.listdir())

# read raw bytes
try:
    with open(full, "rb") as f:
        b = f.read()
except FileNotFoundError:
    print("File not found at that path. Move the file to this folder or use full path.")
    sys.exit(1)

print("\nRaw bytes repr (first 300 bytes):", repr(b[:300]))
print("Raw bytes (hex, first 200 bytes):", b[:200].hex())
print("Length in bytes:", len(b))

# try common decodings
candidates = ["utf-8", "utf-8-sig", "utf-16", "latin-1"]
decoded = None
used_enc = None
for enc in candidates:
    try:
        s = b.decode(enc)
        print(f"\nSuccessfully decoded with: {enc}")
        print("Decoded repr (first 500 chars):", repr(s[:500]))
        decoded = s
        used_enc = enc
        break
    except Exception as e:
        print(f"Could not decode with {enc}: {e}")

if decoded is None:
    print("\nCould not decode file with common encodings. Send me the raw bytes above.")
    sys.exit(1)

# show lines with repr so hidden chars are visible
lines = decoded.splitlines()
print("\nNumber of lines:", len(lines))
for i, line in enumerate(lines, 1):
    print(f"Line {i} repr:", repr(line))

# normalize and search
needle = "rehan"
norm = " ".join(decoded.split()).lower()   # removes extra whitespace and newlines
print("\nNormalized content repr:", repr(norm[:500]))

if needle in norm:
    print("\nRESULT:  Found", needle, "in normalized content.")
elif needle in decoded.lower():
    print("\nRESULT:  Found", needle, "in decoded.lower() (but not in normalized form).")
else:
    print("\nRESULT: NOT FOUND (even after normalizing and lowercasing).")

# if not found, create a test file to ensure writing/reading works
if needle not in norm and needle not in decoded.lower():
    test = os.path.join(os.path.dirname(full), "rehan_test_write.txt")
    with open(test, "w", encoding="utf-8") as f:
        f.write("rehan\n")
    print("\nWrote test file:", test)
    with open(test, "r", encoding="utf-8") as f:
        print("Test file read repr:", repr(f.read()))
    print("\nIf test file contains 'rehan' then Python can read/write fine — your original file probably has")
    print("- different encoding (UTF-16 / BOM) or")
    print("- hidden characters (zero-width spaces) or")
    print("- extra invisible whitespace or different letter-case.")
