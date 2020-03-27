import requests
import json
import xml.etree.ElementTree as ET
'''
SOAP API  v 0.3
'''

base_url = 'http://soap.qa-test.csssr.com:80/ws/'

def xml_body(s):    
    return """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://csssr.com/schemas">
       <soapenv:Header/>
       <soapenv:Body>%s
       </soapenv:Body>
    </soapenv:Envelope>""" % s

def add_company(companyname):
    return """
          <sch:AddCompanyRequest>
             <sch:Name>%s</sch:Name>
          </sch:AddCompanyRequest>""" % companyname

def get_company(compid):
    return """
          <sch:GetCompanyRequest>
         <sch:CompanyId>%s</sch:CompanyId>
      </sch:GetCompanyRequest>""" % compid

def add_empl(firstname, lasname, middlename=None):
    return """
          <sch:AddEmployeeRequest>
             <sch:FirstName>%s</sch:FirstName>
             <sch:LastName>%s</sch:LastName>
             <!--Optional:-->
             <sch:MiddleName>%s</sch:MiddleName>
          </sch:AddEmployeeRequest>""" % (firstname, lasname, middlename if middlename is not None else "" )

def upd_empl(empid, firstname, lasname, middlename=None):
    return """
          <sch:UpdateEmployeeRequest>
             <sch:Id>%s</sch:Id>
             <sch:FirstName>%s</sch:FirstName>
             <sch:LastName>%s</sch:LastName>
             <!--Optional:-->
             <sch:MiddleName>%s</sch:MiddleName>
          </sch:UpdateEmployeeRequest>""" % (empid, firstname, lasname, middlename if middlename is not None else "" )         

def add_empl_to_company(compid, empid):
        return """
          <sch:AddEmployeesToCompanyRequest>
             <sch:CompanyId>%s</sch:CompanyId>
             <!--Zero or more repetitions:-->
             <sch:EmployeeId>%s</sch:EmployeeId>
          </sch:AddEmployeesToCompanyRequest>""" % (compid, empid)

def get_reply(function, *arg):
    x = xml_body(function(*arg))
    r = requests.post(base_url, data=x)
    return r.status_code, r.content       

def company_id_name(y):
    root = ET.fromstring(y[1])
    compid = root.findall('.//{http://csssr.com/schemas}Id')
    compid = compid[0].text
    comp_name = root.findall('.//{http://csssr.com/schemas}Name')
    comp_name = comp_name[0].text
    return compid, comp_name

def empl_id_name(y):
    root = ET.fromstring(y[1])
    compid = root.findall('.//{http://csssr.com/schemas}Id')
    compid = compid[0].text
    comp_name = root.findall('.//{http://csssr.com/schemas}FirstName')
    comp_name = comp_name[0].text
    return compid, comp_name

if __name__ == '__main__':
    
    '''
    x = xml_body(add_company("Parhuman Response Team"))
    print (x)
    x = xml_body(add_empl())
    print (x)
    x = xml_body(add_empl_to_company("11:22","33:44"))
    print (x)
    '''
    y = get_reply(add_empl, "Emely","Pigott")
    print(y[1])
    x = empl_id_name(y)
    print(x)
    




