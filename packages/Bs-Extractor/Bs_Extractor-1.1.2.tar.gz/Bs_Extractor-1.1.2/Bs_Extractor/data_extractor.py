from Bs_Extractor.functions import *
import Bs_Extractor.constants as const
import fitz
from unidecode import unidecode
import re
import numpy as np
import subprocess


class Bs_Extractor:
        
        def __init__(self, pdf_bytes):
                
                self.pdf_bytes = pdf_bytes

        def extract_data(self):
    ### 1. Data Extraction (from pdf) ---------------------------------

            doc = fitz.open(stream=self.pdf_bytes, filetype="pdf")
            plain_text_data = []

            for page in doc:
                page_output = [unidecode(block[4]) for block in page.get_text("blocks") if block[6] == 0]
                if len(page_output)>0:
                    plain_text_data.append(page_output)
                
                
            if plain_text_data:

                plain_text_data=[x for y in plain_text_data for x in y]
                plain_text_data=[ele.strip() for ele in plain_text_data if ele.strip() and ele != '\n']
                plain_text_data=[ele.replace('\n',' ') for ele in plain_text_data]
                
            else:
                ### raise an error : nto a valid file
                
                raise Exception("Unrecognized or Unsupported Document")
                
            most_coomon_datepattern=split_based_on_dates(plain_text_data)[-1]

            plain_text_data=remove_dates_not_matching_format(plain_text_data,most_coomon_datepattern)

            plain_text_data=rearrange_dates_in_list(plain_text_data)


            ### 2. Iban Extraction ---------------------------------

            ##Pattern to match 'AE' followed by 21 digits
            pattern = r'AE\d{21}'

            # Search for the pattern in the provided string
            match = re.search(pattern, ' '.join(plain_text_data))

            # Extracting the matched string
            Iban = match.group(0) if match else None

            rans,most_coomon_datepattern=split_based_on_dates(plain_text_data)[:2]

            if Iban:
                rans=[ele for ele in rans if (len(ele)>20) and (Iban not in ele)]
            else:
                rans=[ele for ele in rans if (len(ele)>20)]
                Iban=''

            ### 3. Processing of Transaction Data  ---------------------------------

            # Regular expression to match the last occurrence of a digit, currency symbol, or 'xx.xx' pattern
            regex_pattern = r"(Cr|Dr|AED|USD|EUR|\b\d+\.\d{2}\b|\d)(?![\s\S]*\d)"

            cleaned_transactions = []
            for transaction in rans:
                match = re.search(regex_pattern, transaction)
                if match:
                    # Truncate the string at the end of the match
                    cleaned_transaction = transaction[:match.end()].strip()
                    cleaned_transactions.append(cleaned_transaction)
                else:
                    # In case no pattern is found, keep the transaction as is
                    cleaned_transactions.append(transaction)
                    
            cleaned_transactions=sort_digits_preserving_order(cleaned_transactions)
            cleaned_transactions=[ele for ele in cleaned_transactions if len(ele)>20]
            cleaned_transactions=extract_elements_with_date(cleaned_transactions,most_coomon_datepattern)
            order = determine_order(cleaned_transactions)
            final_output = sort_list_by_date(cleaned_transactions, most_coomon_datepattern,order)
            extraction_input=filter_elements_with_decimal_digit(final_output)

            ### 4. liquidity Extraction  ---------------------------------

            transaction_sal_liq=filter_elements_with_decimal_digit(extraction_input)
            try:
                
                last_transaction=transaction_sal_liq[-1]
                if 'total' or 'turn over' in transaction_sal_liq[-1].lower():
                    last_transaction=transaction_sal_liq[-2]
                
            except:
                last_transaction=''

            if last_transaction:
                liquidity=extract_liquidity(last_transaction)

                
            ### 5. Salary Extraction  ---------------------------------
                
            regex = re.compile(r"(?:^|[^a-zA-Z])(SAL)(?=[^a-zA-Z]|$)")

            salary = [
                ele.lower() for ele in transaction_sal_liq
                if (
                    "salary" in ele.lower()
                    or (("wps" in ele.lower() or "hr" in ele.lower()) and "sal" in ele.lower())
                    or regex.search(ele)
                )
            ]

            salary=[ele.replace('+','') for ele in salary]

            try:

                avg_salary=round(np.mean([float(extract_salary(ele).replace(',','')) for ele in salary]),2)
                if np.isnan(avg_salary):
                    avg_salary=''
            except:
                avg_salary=''


            ### 6. first transaction date  ---------------------------------

            first_trans_date=extract_date_from_string(extraction_input[0], most_coomon_datepattern)

            ### 7. last transaction date  ---------------------------------

            last_transaction_date=extract_date_from_string(extraction_input[-1], most_coomon_datepattern)

                #### 7.1 check the doc validity:

#---------------------------------# Extract the date from the input string--------------------------------- commented for testing purposes

            # extracted_date_str = re.match(r'\d{2}/\d{2}/\d{4}', last_transaction_date).group()

            # # Parse the extracted date
            # extracted_date = datetime.strptime(extracted_date_str, most_coomon_datepattern)

            # current_date = datetime.now()

            # difference_in_days = (current_date - extracted_date).days

            # # Check if the difference is more than 3 months with a grace period of 1 day
            # is_more_than_3_months = difference_in_days > (90 + 1)

            # if is_more_than_3_months:
            #         raise Exception("Overdated bank statement")

# ---------------------------------  ---------------------------------  ---------------------------------  ---------------------------------  ---------------------------------  



            ### 8. Customer Name Extraction ---------------------------------

            Cust_Name=extract_name(plain_text_data)

            if not Cust_Name:
                try:
                    Cust_Name=' '.join([subele for subele in [ele for ele in plain_text_data if ('account' in ele.lower() and 'name' in ele.lower()) or  ('name' in ele.lower())][0].split(' ') if subele.isupper()])
                    
                except:
                    Cust_Name=''

            ### 9. Account Number Extraction ---------------------------------

            pattern = r'1\d{13}'
            # Search for the pattern in the provided string
            match = re.search(pattern, ' '.join(plain_text_data))

            # Extracting the matched string
            acc_number = match.group(0) if match else None

            #######-------- Final Output -----------
                
            final_json={
                'Iban':Iban,
                'Account_Number':acc_number,
                'liquidity':liquidity,
                'salary':avg_salary,
                'first_trans_date':first_trans_date,
                'last_transaction_date':last_transaction_date,
                'Customer_Name':Cust_Name
                
            }

            return final_json


        def check_pdf_metadata(self):

            try:
                # Run the pdfinfo command with input as bytes
                # print('before run')
                pdfinfo_process = subprocess.run(["pdfinfo", "-"], input=self.pdf_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if pdfinfo_process.returncode != 0:
                    raise Exception("pdfinfo command failed.")
                
                pdfinfo_output = pdfinfo_process.stdout

                # print(pdfinfo_output)
            except FileNotFoundError:
                 raise Exception("pdfinfo command not found. Make sure it's installed and in your PATH.")
                
            # Extract the creator and producer strings, created_at, and modified_at from the pdfinfo output
            creator_string = None
            producer_string = None
            created_at = None
            modified_at = None

            for line in pdfinfo_output.splitlines():
                line_str = line.decode('utf-8')  # Convert bytes to string
                if line_str.startswith("Creator:"):
                    creator_string = line_str[len("Creator:"):].strip()
                elif line_str.startswith("Producer:"):
                    producer_string = line_str[len("Producer:"):].strip()
                elif line_str.startswith("CreationDate:"):
                    created_at = line_str[len("CreationDate:"):].strip()
                elif line_str.startswith("ModDate:"):
                    modified_at = line_str[len("ModDate:"):].strip()

            # crt_list_good= const.creator_lst_good
            # crt_list_bad=const.creator_lst_bad
            # prod_list_good=const.producer_lst_good
            # prod_list_bad=const.producer_lst_bad
            # # Check conditions based on the presence of strings in the lists and created/modified timestamps
            # if creator_string in crt_list_good and producer_string in prod_list_good:
            #     return None
            # elif creator_string in crt_list_good and producer_string in prod_list_bad:
            #      raise Exception("Uploaded an edited PDF")
            # elif creator_string in crt_list_bad and producer_string in prod_list_good:
            #     raise Exception("Uploaded an edited PDF")
            # elif creator_string in crt_list_bad and producer_string in prod_list_bad:
            #      raise Exception("Uploaded an edited PDF")
            # elif creator_string not in crt_list_good + crt_list_bad and producer_string in prod_list_good:
            #     if created_at == modified_at:
            #         return None
            #     else:
            #         raise Exception("Uploaded an edited PDF")
            # elif creator_string not in crt_list_good + crt_list_bad and producer_string in prod_list_bad:
            #     raise Exception("Uploaded an edited PDF")
            # elif creator_string in crt_list_good and producer_string not in prod_list_good + prod_list_bad:
            #     if created_at == modified_at:
            #         return None
            #     else:
            #         return False, "Uploaded an edited PDF"
            # elif creator_string in crt_list_bad and producer_string not in prod_list_good + prod_list_bad:
            #      raise Exception("Uploaded an edited PDF")
            # else:
            #     if created_at == modified_at:
            #         return None
            #     else:
            #         raise Exception("Uploaded an edited PDF")

            meta_data={
            'creator_string':creator_string,
            'producer_string':producer_string,
            'created_at' :created_at,
            'modified_at' :modified_at
            }

            return meta_data