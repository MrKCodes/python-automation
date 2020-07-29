import os
import subprocess
import tarfile
import shutil
import crypt

# Dependencies installations

def installDependencies():
    command1 = "yum",  "-y install *pcre* --nogogcheck"
    command2 = "yum", "-y install *openssl-devel --nogogcheck"
    subprocess.call(command1)
    subprocess.call(command2)
    print("PCRE and Open SSL  dependencies are installed")

def downloadMedia(apacheV, aprV, aprutilV):
    # downloadinf media for apache and apr utils
    apacheTar = apacheV + ".tar.gz"
    aprTar = aprV +".tar.gz"
    aprutilTar = aprutilV + ".tar.gz"

    commandApache = "-c http://www.apache.org/dist/httpd" + apacheTar
    commandApr = "-c http://mirror.cogentco.com/pub/apache/apr/" + aprTar
    commandAprUtils = "-c http://mirror.cogentco.com/pub/apache/apr/" + aprutilTar

    ##
    os.chdir("/usr/src")
    subprocess.call("wget", commandApache)
    subprocess.call("wget", commandApr)
    subprocess.call("wget", commandAprUtils)

    # Apache package extraction
    try:
        print("Extracting Apache TAR")
        tar_apache = tarfile.open(apacheTar)# edit this
        tar_apache.extractall() # specify which folder to extract to
        tar_apache.close()
    except:
        print("Something went wrong")
    

    # Apr package extraction
    try:
        print("Extracting APR TAR")
        tar_apr = tarfile(aprTar)
        tar_apr.extractall()
        tar_apr.close()
    except:
        print("Something went wrong")

    # Apr utils package extraction
    try:
        print("Extracting AprUtils TAR")
        tar_aprutils = tarfile(aprutilTar)
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


def sslCerts():
    # generating certs and key
    print()
"""
def cert_gen(
    
    commonName,
    KEY_FILE,
    CERT_FILE,
    countryName="FR",
    localityName="localityName",
    stateOrProvinceName="IDF",
    organizationName="3DSGS",
    organizationUnitName="Services",
    serialNumber=0,
    validityStartInSeconds=450,
    validityEndInSeconds=10*365*24*60*60,
    ):

    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)
    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = countryName
    cert.get_subject().ST = stateOrProvinceName
    cert.get_subject().L = localityName
    cert.get_subject().O = organizationName
    cert.get_subject().OU = organizationUnitName
    cert.get_subject().CN = commonName
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')
    with open(CERT_FILE, "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open(KEY_FILE, "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))
"""

def copyfile(source,target):
    if(os.path.isfile(source)):
        shutil.copy2(source, target,follow_symlinks=True)
    elif(os.path.isdir(source)):
        shutil.copytree(source,target)
        
def validation():
    # this method will be validating all the configuration
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