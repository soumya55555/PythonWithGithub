import unittest
from UnitTesting.Package1.TC_LoginTest import LoginTest
from UnitTesting.Package2.TC_LogoutTest import LogoutTest
from UnitTesting.Package1.TC_SignUpTest import SignUpTest



#load all the test from test cases
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(LogoutTest)



#catagorize the tcs

SanityTestSuite=unittest.TestSuite([tc1,tc2])
FunctionalTestSuite=unittest.TestSuite([tc3])
MasterTestSuite=unittest.TestSuite([tc1,tc2,tc3])

#unittest.TextTestRunner().run(SanityTestSuite)
#unittest.TextTestRunner().run(FunctionalTestSuite)
unittest.TextTestRunner().run(MasterTestSuite)