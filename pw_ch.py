# getting password from user
def check_password_strength(password): 

    # checking password
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    ## evaluating password
    strength = 0

    # checking length
    if length >= 8:
        strength += 1

    if length >= 12:
        strength += 1
        
    # checking characters types
    if has_upper:
        strength += 1

    if has_lower:
        strength += 1
        
    if has_digit:
        strength += 1
        
    if has_special:
        strength += 1
        
    # avoiding weak passwords
    common_passwords = [
        "password","123456","qwerty","123456789","12345","111111",
        "12345678","password123","654321","guest","123123","1234",
        "thinkpad","default","1234567890","iloveyou","princess",
        "secret","123","123321","test","welcome","ninja","starwars",
        "batman","football","dragon","sunshine","letmein","monkey",
        "superman","chocolate","rainbow","summer","winter","autumn",
        "spring","username","abcdef","helloworld","root","pa$$word",
        "p@$$wOrd","pass123","pass","passwOrd123","myPassword","mypassword",
        "MyPassword","newpassword","newpass","NewPassword","Newpass",
        "strongpassword","weakpassword","randompassword","yourpassword",
        "mysecret","yoursecret","secret123","secretpassword","123password",
        "password1234","password12345","password123456","password1234567",
        "password12345678","password123456789","1234password","54321","000000",
        "1111","2222","3333","4444","5555","6666","7777","8888","9999","112233",
        "abc123","abc","xyz","xyz123","abcxyz","qwertyuiop","asdfghjkl","zxcvbnm",
        "poiuytrewq","lkjhgfdsa","mnbvcxz","qazwsxedc","edcrfvtgby","rfvbgtyhnm",
        "yhnujmikolp","plokmijnuhb","bvgfcxzasd","asdzxcvbnm","mnbvcxzlkjh",
        "lkjhgfdsaqw","qwertyuiopas","poiuytrewqlk","1qaz2wsx3edc","4rfv5tgb6yhn",
        "7ujm8ik9olp","0p9o8i7u6y","5t4r3e2w1q","2qwe3rty4uio","5pas6dfg7hjk","8lzx9cvb0nm",
        "1q2w3e4r5t","6y7u8i9o0p","a1b2c3d4e5","f6g7h8i9j0","k1l2m3n4o5","p6q7r8s9t0",
        "u1v2w3x4y5","z6a7b8c9d0","1a2b3c4d5e","6f7g8h9i0j","k1l2m3n4o5","p6q7r8s9t0",
        "u1v2w3x4y5","z6a7b8c9d0","123abc456","abc123xyz","xyz456abc","456xyz123",
        "123xyzabc","abc456xyz","xyzabc123","456abcxyz","1234abcd5678","abcd1234efgh",
        "efgh5678abcd","5678efgh1234","1234efghabcd","abcdef1234","1234abcdef","abcdefg123",
        "123abcdefg","gfedcba123","123gfedcba","abcdefgh12","12abcdefgh","hgfedcba12",
        "12hgfedcba","password1","password2","password3","password4","password5",
        "password6","password7","password8","password9","password0","1password","2password","3password",
        "4password","5password","6password","7password","8password","9password","0password",
        "password!","password@","password#","password$","password%","password^","password&",
        "password*","password(","password)","!password","@password","#password","$password",
        "%password","^password","&password","*password","(password",")password",
        "password?","password.","password,","password;","password:","password/","password\\",
        "password|","password`","password~","?password",".password",",password",";password",
        ":password","/password","\\password","|password","`password","~password"
    ]

    # checking if password is common
    if password.lower() in common_passwords:
        strength = 0
        
    # feedback based on the strength score
    if strength == 0:
        print("Your password is too short, make sure you put more than 7 characters.")
    elif strength <= 2:
        print("Weak: your password should be longer and include more character types.")
    elif strength <= 4:
        print("Moderate: Your password is okay but could be stronger.")
    elif strength <= 6:
        print("Strong: Your password meets most criteria.")
    else:
        print("Very Strong: Your password is highly secure.")
    
# getting password from user
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
    