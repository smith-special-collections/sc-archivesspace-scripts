import pandas as pd

input_csv = pd.read_csv("CA small accessions-Grid view.csv")

renamed = input_csv.rename(columns={'Descriptive title for accession':'acc_title',
    'Any descriptive information not already stated in the title (optional)':'acc_desc',
    'Gift or transfer?':'acc_type',
    'Date CA received the material (YYYY-MM)':'acc_receipt_date',
    'Donor type':'donor_type',
    'Donor last name':'donor_lastname',
    'Donor first name':'donor_firstname',
    'Donor class year':'donor_classyear',
    'Donor contact - street address':'donor_address',
    'Donor contact - city':'donor_city',
    'Donor contact - state':'donor_state',
    'Donor contact - zip code':'donor_zip',
    'Donor email adress':'donor_email',
    'Donor URI':'donor_uri',
    'Creator type':'creator_type',
    'Creator last name':'creator_lastname',
    'Creator first name':'creator_firstname',
    'Creator class year':'creator_classyear',
    'Creator URI':'creator_uri',
    'Tranferring office':'transfer_office',
    'Transferring office URI':'transfer_office_uri',
    'Related collection':'coll',
    'Related resource URI':'resource_uri',
    'Note if there is a deed, donor letter, transfer form or no supporting documents':'donation_info',
    'Accession identifier':'acc_id_0',
    'Date begin (creation)':'cr_date_begin',
    'Date end (creation)':'cr_date_end',
    'Extent (linear feet)':'extent',
    'Access':'access',
    'Use':'use',
    'Check box to add "immediate source of acquisition" note to AO':'checkbox',
    'Immediate Source of Acquisition':'acq'})
renamed.to_csv("CA_small_acc.csv", index=False)
