import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Give me a hostname(s)')
parser.add_argument('-l', '--list', nargs='+', help='<Required> Set flag', required=True, dest='hosts')
args = parser.parse_args()


def main():
    os.system('wget https://redos.red-soft.ru/support/secure/redos.xml')
    output = subprocess.check_output("oscap info redos.xml", shell=True)
    for i in args.hosts:
        os.system(
            'oscap-ssh user@{} 22 oval eval --skip-validation --results results.xml --report {}.html redos.xml'.format(
                i, i))
        os.system('cp *.html /tmp')

def another_way():
    for i in args.hosts:
        os.system(
            'oscap-ssh user@{} 22 oval eval --skip-validation --results results.xml --report {}.html redos_orig.xml'.format(
                i, i))
        os.system('cp *.html /tmp')


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError:
        print('\x1b[6;30;42m' + '(ERROR)Check file, coz he is broken. I will use good file redos.xml' + '\x1b[0m')

    try:
        another_way()
    except:
        print('\x1b[6;30;42m' + '(ERROR)Something wrong' + '\x1b[0m')