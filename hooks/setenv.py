import sys
import shutil
import os

def getpostgresqlenv(options,buildout):
    os.environ['EXTRA_LDAP_LIBS'] = os.environ['LDFLAGS']
    
    
def getpostgresqlenv(options,buildout):
    os.environ['EXTRA_LDAP_LIBS'] = os.environ['LDFLAGS']
    
def p(o, b):
    if 'win' in sys.platform:
        dest = o['location']
        lib = os.path.join(dest, 'lib')
        bin = os.path.join(dest, 'bin')
        for dll in [libdll 
                    for libdll in os.listdir(lib) 
                    if libdll.endswith('dll')]:
            orig, ldest = os.path.join(lib, dll), os.path.join(bin, dll)
            if os.path.exists(ldest):
                os.remove(ldest)
            shutil.copy2(orig, ldest)

    
# vim:set ts=4 sts=4 et  :