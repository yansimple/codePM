# by YANSIMPLE
from path import prettyPATH

enter1 = "/var/test/../lib/./foo"
exit1 = "/var/lib/foo"

enter2 = "/home/.././some/rev/foo"
exit2 = '/some/rev/foo'

enter3 = '../some/sh/it/.'
exit3 = '/some/sh/it'

enter4 = '/var/../test/sap/../lib/./foo'
exit4 = '/lib/foo'

enter5 = '/user/./date/../root/man/foo'
exit5 = '/user/root/man/foo'

if prettyPATH(enter1) == exit1:
    print("test 1 = right!")
else:
    print("test 1 = wrong!")

if prettyPATH(enter1) == exit1:
    print("test 2 = right!")
else:
    print("test 2 = wrong!")

if prettyPATH(enter3) == exit3:
    print("test 3 = right!")
else:
    print("test 3 = wrong!")

if prettyPATH(enter4) == exit4:
    print("test 4 = right!")
else:
    print("test 4 = wrong!")

if prettyPATH(enter5) == exit5:
    print("test 5 = right!")
else:
    print("test 5 = wrong!")
