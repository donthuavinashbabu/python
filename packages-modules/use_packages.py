from MainPackage import main_package

# from MainPackage.SubPackage1 import sub_package_1
# from MainPackage.SubPackage1.sub_package_1 import sub_report2

# If we import sub_report2 in __init__.py. Refer SubPackage1.__init__.py
from MainPackage.SubPackage1 import sub_package_1, sub_report2

main_package.main_report()
sub_package_1.sub_report1()
sub_report2()

# py use_packages.py
# I am MainPackage.main_report
# I am SubPackage1.sub_report1
# I am SubPackage1.sub_report2