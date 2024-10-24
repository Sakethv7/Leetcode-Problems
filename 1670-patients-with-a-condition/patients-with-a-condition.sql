# Write your MySQL query statement below
#patient_id, pateint_name and conditions  who have type 1 diabetes.
#Type 1 has DIAB1 prefix

select
    patient_id, patient_name,
    conditions
from 
    patients
    where conditions regexp '(^| )DIAB1[0-9]*(|$)';

    #regexp returns the query which has the expression 'x': where row_name regexp 'x'
    #
-- Matches either the start of the string (^) or a space ( ), ensuring that DIAB1 is either at the start or preceded by a space.
-- DIAB1:
-- Matches the literal string "DIAB1".
-- [0-9]*:
-- Matches zero or more digits following "DIAB1".