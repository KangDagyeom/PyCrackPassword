from random import choice
import os

u_pwd = input("Enter a password: ")
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
       '1', '2', '3', '4', '5', '6', 
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
       '!', '@', '#', '$', '%', '^', '&', '*']

pw = ""
while pw != u_pwd:
    pw = "".join(choice(pwd) for _ in range(len(u_pwd)))  # Tạo mật khẩu ngẫu nhiên có độ dài bằng mật khẩu người dùng
    
    print("Current guess:", pw)
    print("Cracking Password...Please Wait")
    os.system("cls" if os.name == 'nt' else 'clear')

print("Your Password Is:", pw)