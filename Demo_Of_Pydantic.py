def insert_patient_data(name:str, age:int):
    if type(name) ==  str and type(age) == int:
        print(name)
        print(age)
        print('Data Inserted')
        
    else:
        raise TypeError('Incorrect Data Type')


insert_patient_data('Ashish', 30)