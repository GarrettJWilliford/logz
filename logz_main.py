import datetime
import getpass
import socket
import os
import uuid
import base64
import hashlib
from cryptography.fernet import Fernet



def log_writer():
    os.system('cls')
    date_created = str(datetime.datetime.now())
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    user = getpass.getuser()
    log = []
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|LOGZ|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    log_title = input('log_title     : ')
    log_type =  input('log_type      : ')
    print('date_created  : ' + date_created)
    print('date_modified : ' + date_created)
    print('user          : ' + user)
    print('host          : ' + host_name)
    print('ip_address    : ' + ip_address)
    print('encrypted     : ' + 'False')
    print('----------------------------------------------------------------------------')
    while True:
        current_line = input('')
        if current_line == '/LOG':
            break
        log.append(current_line)
    
    return {
    'title'         : log_title,
    'file_type'     : 'log',
    'date_created'  : date_created,
    'date_modified' : date_created,
    'created_by'    : user,
    'file_id'       : str(uuid.uuid4()),
    'file_contents' : {
        'title'        : log_title,
        'log_type'     : log_type,
        'date_created' : date_created,
        'date_modified': date_created,
        'host'         : host_name,
        'ip'           : ip_address,
        'encrypted'    : False,
        'log'          : log
        }
    }



def log_reader(log_file):
    os.system('cls')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|LOGZ|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('log_title     : ' + log_file['file_contents']['title'])
    print('log_type      : ' + log_file['file_contents']['log_type'])
    print('date_created  : ' + log_file['file_contents']['date_created'])
    print('date_modified : ' + log_file['file_contents']['date_modified'])
    print('user          : ' + log_file['created_by'])
    print('host          : ' + log_file['file_contents']['host'])
    print('ip_address    : ' + log_file['file_contents']['ip'])
    print('encrypted     : ' + str(log_file['file_contents']['encrypted']))
    print('----------------------------------------------------------------------------')
    for line in log_file['file_contents']['log']:
        print(str(line))
    print('----------------------------------------------------------------------------')
    exit_command = input('')




def encrypt_password(password):
    password = bytes(password)
    hlib = hashlib.md5()
    hlib.update(password)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))



def encrypt_log(password, log):
    encryption_key = encrypt_password(password)
    fernet_encryption = Fernet(encryption_key)
    log['file_contents']['log'] = [fernet_encryption.encrypt(line.encode('utf-8')).decode() for line in log['file_contents']['log']]
    log['file_contents']['date_modified'] = str(datetime.datetime.now())
    log['file_contents']['encrypted'] = True



def decrypt_log(password, log):
    encryption_key = encrypt_password(password)
    fernet_encryption = Fernet(encryption_key)
    log['file_contents']['log'] = [fernet_encryption.decrypt(line.encode('utf-8')).decode() for line in log['file_contents']['log']]
    log['file_contents']['date_modified'] = str(datetime.datetime.now())
    log['file_contents']['encrypted'] = False

















