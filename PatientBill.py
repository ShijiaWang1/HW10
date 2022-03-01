
from unicodedata import name
from webbrowser import get
import PatientClass as p
import ProcedureClass as pro


def main():

    ID= 1

    name= 'Matt Jones'
    
    address= '123 Main st, Waco TX 76706'
    
    phone= '254-555-7415'
    
    veteran_status= 'TRUE'

    patient= p.Patient(ID, name, address, phone, veteran_status)

    print('patient_id\tname\t\taddress\t\t\tphone\t\tveteran_status','\n',
    patient.get_ID(),'\t',
    '    ',patient.get_name(),
    '  ',patient.get_address(),
    patient.get_phone(),
    '\t',patient.get_veteran_status(),'\n')


    procedure_1= pro.Procedure('Physica Exam','02/15/2022','Dr.Irvine',250,1)
    procedure_2= pro.Procedure('MRI','02/15/2022','Dr.Irvine',1500,1)
    procedure_3= pro.Procedure('CT Scan','02/15/2022','Dr.Irvine',1200,2)
    

    procedure_list= [procedure_1,procedure_2,procedure_3]

    print('***Patient Bill***')
    print('Name: ',patient.get_name())
    print('Address: ',patient.get_address())
    print('Phone: ',patient.get_phone())
    print('\n')


    for procedure in (procedure_list):
        if procedure.get_patient_ID() == ID:
            print('Porcedure: ',procedure.get_pname(),'\n',
            'Date: ',procedure.get_date(),'\n',
            'Practitioner: ',procedure.get_practitioner(),'\n',
            'Charge: ',procedure.get_charges(),'\n',
            )
        

            print('Total Charges: ')


main()