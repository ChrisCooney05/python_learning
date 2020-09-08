import csv
import json

compromised_users = []

with open('./files_py/passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password in password_csv:
        compromised_users.append(password['Username'])
print(compromised_users)
# Reads passwords.csv and adds the username to the list of compromised_users

with open('./files_py/compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + '\n')
# Not including the '\n' produces one long ugly string
# This will overwrite the file if it exists or make a new one if it does not. 'w' stands for write, if we want to add
# to the file we can use 'a' for append.

with open('./files_py/boss_message.json', 'w') as boss_message:
    boss_message_dict = {
        'recipient': 'The Boss',
        'Message': 'Mission Success'
    }
    json.dump(boss_message_dict, boss_message)
# Makes a json file or overwrites if it already exists, dictionairy is the first argument file target is the second

with open('./files_py/passwords.csv', 'a') as new_passwords_obj:
    slash_null_sig = '''
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''
    new_passwords_obj.write(slash_null_sig)

# Running this file once more with 'w' will delete the passwords.csv and replace it with our slash_null_sig string.
# using 'a' as an argument to show how it works
