import getopt
import sys
import os
import subprocess
import re
re_odj = "Id:([\s\S]*?)Name[\s\S]*?UUID:([\s\S]*?)OS"
find_vnc_cmd = "virsh vncdisplay "
gen_vm_info_cmd = "for i in `virsh list | awk {' print $1 '} | grep -v Id`;do virsh dominfo $i;done > /home/lxy/vm_info"


def print_help():
    print """
    command:

    python find_vm_vnc.py --uuid 12345
    python find_vm_vnc.py --uuid 1234,3625 
 
    """


def exec_cmd(cmd):
    result = None
    try:
        result = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        return e.returncode, result
    return 0, result


def gen_dict():
    d = {}
    try:
        with open("./vm_info",'r') as f:
            pattern = re.compile(re_odj)
            data = re.findall(pattern,f.read())
            for id,uuid in data:
                id = id.strip()
                uuid = uuid.strip()
                d[uuid] = id
    except Exception as e:
        print(e)
    return d


def find_vm_id(uuid):
    new_dict = gen_dict()
    for key in new_dict.keys():
        if key.find(uuid) != -1:
            id = new_dict[key]
            return id


def write_vm_info(result):
    with open("./vm_vnc_info","a") as f:
	    f.write(result+"\n") 


def read_vm_vnc_info():
    with open("./vm_vnc_info","r") as f:
	    for line in f:
	        if line!="\n":
	  	    print(line)

def main():
    try:
        ret, result = exec_cmd(gen_vm_info_cmd)
    except Exception as e:
	    pass
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ncsvh", ["uuid=","help"])
    except getopt.GetoptError, err:
        print str(err)
        print_help()
        sys.exit(2)
    if len(opts) == 0:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("--uuid"):
            uuid = arg
            for i in uuid.split(','):
                id = find_vm_id(i)
                ret, result = exec_cmd(find_vnc_cmd+id)
                write_vm_info(i+result)
    read_vm_vnc_info()

    if opt in ("-h","--help"):
        print_help()
        sys.exit()
    try:
        os.remove("./vm_vnc_info")
    except:
        pass

if __name__ == '__main__':
    main()

