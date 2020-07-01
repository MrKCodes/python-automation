import os
import subprocess
import tarfile
import shutil

# Dependencies installations

def installDependencies():
    command1 = "yum",  "-y install *pcre* --nogogcheck"
    command2 = "yum", "-y install *openssl-devel --nogogcheck"
    subprocess.call(command1)
    subprocess.call(command2)
    print("PCRE and Open SSL  dependencies are installed")

def downloadMedia(apacheV, aprV, aprutilV):
    # downloadinf media for apache and apr utils
    commandApache = "-c http://www.apache.org/dist/httpd" + apacheV + ".tar.gz"
    commandApr = "-c http://mirror.cogentco.com/pub/apache/apr/" + aprV +".tar.gz"
    commandAprUtils = "-c http://mirror.cogentco.com/pub/apache/apr/" + aprutilV + ".tar.gz"

    ##
    os.chdir("/usr/src")
    subprocess.call("wget", commandApache)
    subprocess.call("wget", commandApr)
    subprocess.call("wget", commandAprUtils)

    # Apache package extraction
    try:
        print("Extracting Apache TAR")
        tar_apache = tarfile.open(apacheV)
        tar_apache.extractall() # specify which folder to extract to
        tar_apache.close()
    except:
        print("Something went wrong")
    

    # Apr package extraction
    try:
        print("Extracting APR TAR")
        tar_apr = tarfile(aprV)
        tar_apr.extractall()
        tar_apr.close()
    except:
        print("Something went wrong")

    # Apr utils package extraction
    try:
        print("Extracting AprUtils TAR")
        tar_aprutils = tarfile(aprutilV)
        tar_aprutils.extractall()
        tar_aprutils.close()
    except:
        print("Something went wrong")

    print("Moving the apr and apr-utils to apache source")
    destination = "/usr/src/" + apacheV
    ## Moving apr and aprutils to use/src/httpd-2.4
    shutil.move(aprV, destination)
    shutil.move(aprutilV, destination)

def compileSrc(apacheSrc):
    # apacheSrc is the apache path as /usr/src/httpd2.4.25
    os.chdir(apacheSrc)
    try:
        configure = "./configure", "--enable-so --enable-ssl --with-mpm=prefork --with-included-apr"
        subprocess.call(configure)
        subprocess.call("make")
        subprocess.call("make", "install")
    except:
        print("Something went wrong")

def postInstall():
    # Will contain modules like:
    ## enable ssl by editing httpd.conf
    ## start apache
    ## enable socache_shmcb
    ## copy the keys and certs
    ## 
    print()




# Main module

if __name__ ==  "__main__":
    print("Executing main Module")
    
    #Dependencies
    installDependencies()

    # Installable downloads and Extraction from tar.gz
    downloadMedia("httpd-2.4.43", "apr-1.6.5", "apr-util-1.6.1")

    # Compiling the source - Installing the apache
    compileSrc("/usr/src/httpd-2.4.43")

    # post Installation steps
    postInstall()