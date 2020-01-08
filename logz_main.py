import pickle
from ethropic_encryption import *
import getpass
import pandas as pd
import datetime
import os
import re



#pickle.dump('<<!NO_NAME!>>', open('key_check.p', 'wb'))






def login_init():
    key = getpass.getpass(prompt = '>>ENTER_KEY>> ')
    command = getpass.getpass(prompt = '>>ENTER_LOGIN>> ')
    if command == d_1(key, pickle.load(open('passw0rd.p', 'rb'))):
        pickle.dump(key, open('key_check.p', 'wb'))
        print('<<|LOGIN_ACCEPTED|>>')
        return True
    print('<<!LOGIN_DENIED!>>')
    return False

##########_RUN_THIS_TO_INIATE_THE_LOGZ_PROGRAM_############
#login_init()
############################################################


#def security_check():
 #   if d_1(pickle.load(open('key_check.p', 'rb'), pickle.load(open('security_question.p', 'rb'))) == 'fitness_gram_pacer_test':
  #         print('!')
                


def logz_hard_reset():
    security = security_check()
    if security == True:
        print('<<!DELETE_ALL_LOGS!>>')
        a = input('>>|ENTER_CONFIRM_TO_CONTINUE|>> ')
        if a == 'CONFIRM':
            pickle.dump({} , open('logset.p', 'wb'))
            done = input('<<|LOGS_RESET|>>')
            return
        done = input('<<|COMMAND_CANCELD|>>')
        return

def logz_backup():
    while True:
        while True:
            print('<<|BACKUP_ENCRYPTED?|>>')
            command = input('>>|[Y]es/[N]o|>> ')
            if command == 'Y':
                encrypt = True
                break
            if command == 'N':
                encrypt = False
                break
        file_name = input('>>|ENTER_FILE_NAME|>> ')
        try:
            if encrypt:
                pickle.dump(pickle.load(open('logset.p', 'rb'), open(file_name, 'wb')))
            if not_encrypt:
                pickle.dump(d_1(pickle.load(open('key_check.p', 'rb')), pickle.load(open('logset.p', 'rb'))), open(str(file_name), 'wb'))
            done = input('<<|FILE_SAVED|>>')
            return
        except:
            error = input('<<!ERROR|INVALID_FILE_NAME!>>')
            continue

def decrypt_logs():
    decrypted_logs = {}
    encrypted_logs = pickle.load(open('logset.p', 'rb'))
    for logs in encrypted_logs:
        de.update(d_1(encrypted_logs[logs]))
                              


def logz():
    commands = ['READ_LOG', 'NEW_LOG', 'REMOVE_LOG', 'BACK']
    if pickle.load(open('key_check.p', 'rb')) == '<<!NO_NAME!>>':
        print('<<!LOGIN_REQUIRED!>>')
        return
    while True:
        os.system('clear')
        print('<<<<<<<<<<<<<<<<<<<<<<<LOGZ>>>>>>>>>>>>>>>>>>>>>>>')
        key = pickle.load(open('key_check.p', 'rb'))
        try:
            logset = pickle.load(open('logset.p', 'rb'))
        except:
            print('<<!ERROR|NO_LOGS_FOUND!>>')
            logset = {}
        try:
            log_id = 0
            for l in logset:
                log_id += 1
                print('{:2}| {}    || {}'.format(l, d_1(key, logset[l][0]), d_1(key, logset[l][1][0])))
        except:
            print('<<!ERROR|LOGS_CANNOT_BE_DISPLAYED!>>')
            pass
        print('<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>')
        for c in commands:
            print('>>| ' + c)
        print('<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')
        command = input('>>ENTER_COMMAND>> ')
        if command == 'NEW_LOG':
            log = []
            os.system('clear')
            time = datetime.datetime.now()
            print(time)
            print('<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')
            while True:
                line = input('')
                try:
                    log.append(e_1(key, line))
                except:
                    log.append(e_1(key, '<CORRUPTED>'))
                if line == '/LOG':
                    #str(int(sorted(logset.keys())[-1]) + 1)

                    try:
                        logset.update({str(int(sorted([int(l) for l in logset.keys()])[-1]) + 1) : [e_1(key, str(time)), log]})
                    except:
                        logset.update({'0' : [e_1(key, str(time)), log]})
                    pickle.dump(logset, open('logset.p', 'wb'))
                    break
        if command[0:10] == 'REMOVE_LOG':
            remove_num = (''.join([c for c in command if c.isdigit()]))
            while True:
                print('<<!REMOVE_LOG_%s?!>>' % remove_num)
                confirm = input('>>[Y]es/[N]o>> ')
                if confirm == 'Y':
                    del logset[remove_num]
                    pickle.dump(logset, open('logset.p', 'wb'))
                    deleted = input('<<|LOG_DELETED|>>')
                    break
                if confirm == 'N':
                    cancel = input('<<|COMMAND_CANCELD|>>')
                    break
                else:
                    print('<<|INVALID_ENTRY|>>')
        if command == 'BACK':
            return
        if command[0:8] == 'READ_LOG':
            os.system('clear')
            try:
                c = (''.join([c for c in command if c.isdigit()]))
                print(c)
                print('<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')
                print(d_1(key, logset[c][0]))
                for l in logset[c][1]:
                    print(re.sub('_', ' ', d_1(key, l)))
                print('<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>')                
            except:
                print('<<!ERROR|LOG_NOT_FOUND!>>')
            command = input('')
        
