import os
import subprocess
import tarfile



# Dependencies installations

def installDependencies():
    command1 = "yum",  "-y install *pcre* --nogogcheck"
    command2 = "yum", "-y install *openssl-devel --nogogcheck"
    subprocess.call(command1)
    subprocess.call(command2)
    print("PCRE and Open SSL  dependencies are installed")

def downloadMedia():
    # downloadinf media for apachae and apr utils
    commandApache = "wget", "-c "
    commandApr = "wget", "-c "
    commandAprUtils = "wget","-c "

    ##
    os.chdir("/usr/src")