# Personal Vault & Password Analyzer

def encrypt(text):
    """Caesar Cipher का उपयोग करके टेक्स्ट को एनक्रिप्ट करता है (Shift 1)"""
    encrypted = ""
    for char in text:
        encrypted += chr(ord(char) + 1)
    return encrypted

def decrypt(text):
    """एनक्रिप्टेड टेक्स्ट को वापस सामान्य बनाता है"""
    decrypted = ""
    for char in text:
        decrypted += chr(ord(char) - 1)
    return decrypted

def check_strength(password):
    """पासवर्ड की मजबूती की जांच करता है"""
    has_number = False
    has_special = False
    special_chars = "@#$%&!*"
    numbers = "0123456789"

    if len(password) < 8:
        return "Weak (8 अक्षरों से कम है)"

    # इंटरव्यूअर का चैलेंज: बिना किसी मॉड्यूल के नंबर चेक करना
    for char in password:
        if char in numbers:
            has_number = True
        if char in special_chars:
            has_special = True

    if not has_number or not has_special:
        return "Medium (नंबर या स्पेशल कैरेक्टर शामिल करें)"
    
    return "Strong"

def main():
    master_password = "admin" # आपका मास्टर पासवर्ड
    
    print("--- Personal Vault में आपका स्वागत है ---")
    entry = input("मास्टर पासवर्ड दर्ज करें: ")

    if entry != master_password:
        print("गलत पासवर्ड! एक्सेस वर्जित है।")
        return

    vault_data = []

    while True:
        print("\n1. नया सीक्रेट नोट जोड़ें\n2. नोट्स देखें\n3. बाहर निकलें")
        choice = input("विकल्प चुनें: ")

        if choice == '1':
            note = input("अपना नोट या पासवर्ड लिखें: ")
            strength = check_strength(note)
            
            if strength == "Strong":
                encrypted_note = encrypt(note)
                vault_data.append(encrypted_note)
                print("सफलतापूर्वक 'Strong' पासवर्ड के रूप में सेव किया गया!")
            else:
                print(f"सुरक्षा चेतावनी: आपका पासवर्ड {strength} है। कृपया बेहतर पासवर्ड चुनें।")

        elif choice == '2':
            print("\n--- आपके सुरक्षित नोट्स ---")
            for item in vault_data:
                print(f"सुरक्षित डेटा: {item} | असली डेटा: {decrypt(item)}")
        
        elif choice == '3':
            break
        else:
            print("अमान्य विकल्प!")

if __name__ == "__main__":
    main()
      
