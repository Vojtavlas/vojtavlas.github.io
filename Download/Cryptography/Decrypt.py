hash = "08a841e996781e9e77d30a4e4420a8f501a280b00624e6d1224bf54aaff73eba"
import hashlib
hash1 = ""
with open(r'C:\Users\Vojtěch Vlasák\Desktop\Coding\Cryptography\password.txt', 'r') as file:
    lines = file.readlines()
    for i in range(500):
        var_text = lines[i].strip()
        hash1 = hashlib.sha256(b"" + var_text).hexdigest()
        if hash1 == hash:
            print(f"Success:{hash}")