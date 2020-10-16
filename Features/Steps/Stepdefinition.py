from behave import *
from selenium import webdriver


@given(u'Launch the browser')
#def step_impl(context):
def Launcnbrowser(context):
 context.driver = webdriver.Chrome(executable_path = "C:\\Users\\KRISHNA PC\\Desktop\\Testing\\downloads\\chromedriver.exe")

@when(u'Open the OHRM homepage')
def step_impl(context):




@then(u'Verify logo presence')
def step_impl(context):



@then(u'Close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Close browser')
