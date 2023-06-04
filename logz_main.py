import datetime
import getpass
import socket
import os
from cryptography.fernet import Fernet
import uuid
import base64
import hashlib

class logs:
    def __init__(self):
        self.logz = {
            'logs_information' : 
            {
                'created_by'   : getpass.getuser(),
                'date_created' : str(datetime.datetime.now()), 
                'date_modified' : str(datetime.datetime.now()),
                
            },
            'logs' : []
        }

    def _encrypt_password(self, password):
        password = bytes(password)
        hlib = hashlib.md5()
        hlib.update(password)
        return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

    def write_log(self):
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
        
        self.logz['logs'].append({
            'title'        : log_title,
            'log_type'     : log_type,
            'date_created' : date_created,
            'date_modified': date_created,
            'user'         : user,
            'host'         : host_name,
            'ip'           : ip_address,
            'encrypted'    : False,
            'log'          : log
            })
    
    def read_log(self, log_index):
        os.system('cls')
        log_file = self.logz['logs'][log_index]
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|LOGZ|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print('log_title     : ' + log_file['title'])
        print('log_type      : ' + log_file['log_type'])
        print('date_created  : ' + log_file['date_created'])
        print('date_modified : ' + log_file['date_modified'])
        print('user          : ' + log_file['user'])
        print('host          : ' + log_file['host'])
        print('ip_address    : ' + log_file['ip'])
        print('encrypted     : ' + str(log_file['encrypted']))
        print('----------------------------------------------------------------------------')
        for line in log_file['log']:
            print(str(line))
        print('----------------------------------------------------------------------------')
        exit_command = input('')
    
    def encrypt_log(self, password, log_index):
        encryption_key = self._encrypt_password(password)
        fernet_encryption = Fernet(encryption_key)
        self.logz['logs'][log_index]['log'] = [fernet_encryption.encrypt(line.encode('utf-8')).decode() for line in self.logz['logs'][log_index]['log']]
        self.logz['logs'][log_index]['date_modified'] = str(datetime.datetime.now())
        self.logz['logs'][log_index]['encrypted'] = True
    
    def encrypt_all_logs(self, password):
        for log_index in range(len(self.logz['logs'])):
            self.logz['logs'][log_index] =  self.encrypt_log(password, self.logz['logs'][log_index])

    def decrypt_log(self, password, log_index):
        encryption_key = self._encrypt_password(password)
        fernet_encryption = Fernet(encryption_key)
        self.logz['logs'][log_index]['log'] = [fernet_encryption.decrypt(line.encode('utf-8')).decode() for line in self.logz['logs'][log_index]['log']]
        self.logz['logs'][log_index]['date_modified'] = str(datetime.datetime.now())
        self.logz['logs'][log_index]['encrypted'] = False

    def decrypt_all_logs(self, password):
        for log_index in range(len(self.logz['logs'])):
            self.logz['logs'][log_index] =  self.decrypt_log(password, self.logz['logs'][log_index])
    
