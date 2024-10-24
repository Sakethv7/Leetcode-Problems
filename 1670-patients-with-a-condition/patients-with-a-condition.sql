# Write your MySQL query statement below
#patient_id, pateint_name and conditions  who have type 1 diabetes.
#Type 1 has DIAB1 prefix

select
    patient_id, patient_name,
    conditions
from 
    patients
    where conditions regexp '(^| )DIAB1[0-9]*';

    #regexp returns the query which has the expression 'x': where row_name regexp 'x'

