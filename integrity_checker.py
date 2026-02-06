import hashlib
import os
import sys

def sha256_file(path, chunk_size=1024 * 1024):
    """Compute SHA-256 of a file in chunks (memory safe for large files)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: python integrity_checker.py <file_path> [expected_hash]")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("Error: File not found.")
        sys.exit(1)

    computed = sha256_file(file_path)
    print(f"SHA-256: {computed}")

    # Optional verification
    if len(sys.argv) >= 3:
        expected = sys.argv[2].lower().strip()
        if computed == expected:
            print("✅ Hash matches. File integrity OK.")
        else:
            print("❌ Hash mismatch! File may be altered or corrupted.")

if __name__ == "__main__":
    main()