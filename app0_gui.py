"""
app0.py illustrates use of pitaxcalc-demo release 2.0.0 (India version).
USAGE: python app0.py > app0.res
CHECK: Use your favorite Windows diff utility to confirm that app0.res is
       the same as the app0.out file that is in the repository.
"""
from taxcalc import *

# create Records object containing pit.csv and pit_weights.csv input data
recs = Records()

assert isinstance(recs, Records)
assert recs.data_year == 2018
assert recs.current_year == 2018
"""
# create GSTRecords object containing gst.csv and gst_weights.csv input data
grecs = GSTRecords()

assert isinstance(grecs, GSTRecords)
assert grecs.data_year == 2018
assert grecs.current_year == 2018

# create CorpRecords object containing cit.csv and cit_weights.csv input data
crecs = CorpRecords()

assert isinstance(crecs, CorpRecords)
assert crecs.data_year == 2018
assert crecs.current_year == 2018

policy_filename = "current_law_policy_cmie.json"
# create Policy object containing current-law policy
pol = Policy(DEFAULTS_FILENAME=policy_filename)
"""
pol = Policy()

assert isinstance(pol, Policy)
assert pol.current_year == 2018

# specify Calculator object for current-law policy
#calc1 = Calculator(policy=pol, records=recs, gstrecords=grecs,
#                   corprecords=crecs, verbose=False)

calc1 = Calculator(policy=pol, records=recs, verbose=False)

# NOTE: calc1 now contains a PRIVATE COPY of pol and a PRIVATE COPY of recs,
#       so we can continue to use pol and recs in this script without any
#       concern about side effects from Calculator method calls on calc1.

assert isinstance(calc1, Calculator)
assert calc1.current_year == 2018

for year in range(2018, 2021):
    calc1.advance_to_year(year)
    calc1.calc_all()
    """
    dump_vars = ['id_n','EmpIncCages10', 'EmpInc', 
                 'ReliefEmpIncomeCages60', 'ReliefEmpIncomeAllowed',
                 'ReliefForeignIncomeCages70','ReliefForeignIncomeAllowed',
                 'ReliefRentIncomeCages80', 'ReliefRentalIncomeAllowed',
                 'ReliefInterestIncomeCages90', 'ReliefInterestIncomeAllowed',
                 'PersonalReliefCages100', 'PersonalReliefAllowed',
                 'QualifyingPaymentCages120', 'QualifyingPaymentAllowed',
                 'TotalReliefCages110', 'TotalRelief', 'TotalTaxPayableCages190','pitax']
    dumpdf = calc1.dataframe(dump_vars)
    column_order = dumpdf.columns
    
    assert len(dumpdf.index) == calc1.array_len
    
    dumpdf.to_csv('app0-dump.csv', columns=column_order,
                  index=False, float_format='%.0f')
    """
    print(calc1.weighted_total_pit('pitax'))
