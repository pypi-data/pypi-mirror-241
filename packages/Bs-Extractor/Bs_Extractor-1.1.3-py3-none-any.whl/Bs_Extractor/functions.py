import re
from collections import Counter
from datetime import datetime

### Define functions

def pdf_to_bytes(pdf_file_path):
#     try:
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        return pdf_bytes

def sort_digits_preserving_order(strings):
    sorted_strings = []

    for s in strings:
        words = s.split()
        digit_words = [word for word in words if '.' in word and word.replace('.', '').replace(',', '').isdigit()]
        non_digit_words = [word for word in words if word not in digit_words]

        sorted_string = ' '.join(non_digit_words + digit_words)
        sorted_strings.append(sorted_string)

    return sorted_strings

def split_based_on_dates(text_list):
    joined_text = ' '.join(text_list)

    date_regex = re.compile(
   r'(?<![.\d])(\b\d{2}/\d{2}/\d{4}\b'  # DD/MM/YYYY
    r'|\b\d{2}-[a-zA-Z]{3}-\d{4}\b'  # DD-MMM-YYYY
    r'|\b\d{4}-\d{2}-\d{2}\b'  # YYYY-MM-DD
    r'|\b\d{2}[a-zA-Z]{3}\d{2}\b'  # DDMMMYY
    r'|\b\d{1,2}\s(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\b'  # D or DD MMM YYYY
    r'|\b\d{2}\s[a-zA-Z]{3}\s\d{2}\b'  # DD MMM YY
    r'|\b\d{2}-\d{2}-\d{4}\b'  # DD-MM-YYYY
    r'|\b\d{2}-\d{1,2}-\d{4}\b'  # DD-M-YYYY or D-MM-YYYY
    r'|\b\d{1,2}-[a-zA-Z]{3}-\d{2}\b)(?![.\d])'  # D or DD-MMM-YY
)

    # Find all matches of date patterns
    matches = [match for match in re.finditer(date_regex, joined_text)]

    if not matches:
        return [joined_text], None  # Return the original text if no dates are found
    
    def determine_format(date_str):
        for fmt in (
    "%d/%m/%Y",  # DD/MM/YYYY
    "%d-%b-%Y",  # DD-MMM-YYYY
    "%Y-%m-%d",  # YYYY-MM-DD
    "%d%b%y",    # DDMMMYY
    "%d %b %Y",  # DD MMM YYYY
    "%d %b %y",  # DD MMM YY
    "%d-%m-%Y",  # DD-MM-YYYY
    "%d-%b-%y",  # DD-MMM-YY
    # Add any other formats that you have in your regex
):
            try:
                datetime.strptime(date_str, fmt)
                return fmt
            except ValueError:
                continue
        return None
   # Function to check if the string is a valid date according to given formats
    def is_valid_date(date_str):
        for fmt in (
            "%d/%m/%Y", "%d-%b-%Y", "%Y-%m-%d", "%d%b%y", "%d %b %Y", "%d %b %y",
            "%d-%m-%Y", "%d-%b-%y", # Add any other formats that you have in your regex
        ):
            try:
                datetime.strptime(date_str, fmt)
                return True
            except ValueError:
                continue
        return False
    matches = [match for match in re.finditer(date_regex, joined_text) if is_valid_date(match.group(0))]
    # Determine formats for all matches
    formats = [determine_format(match.group(0)) for match in matches]
    formats=[ele for ele in formats if ele is not None]
    # Find the most common format
    most_common_format = Counter(formats).most_common(1)[0][0]

    # Split the text into segments
    segments = []
    start_index = 0
    for i, match in enumerate(matches):
        end_index = matches[i + 1].start() if i + 1 < len(matches) else len(joined_text)
        segment = joined_text[match.start():end_index].strip()
        segments.append(segment)
        start_index = end_index

    return segments, most_common_format


def rearrange_dates_in_list(text_list):
    """
    Rearranges each element in a list by moving the first date found to the beginning of the string.

    :param text_list: List of strings to be processed.
    :param date_regex: Compiled regular expression to match date patterns.
    :return: List with rearranged strings.
    """
    # Define the date patterns and compile the regex
    date_patterns = r'\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-[a-zA-Z]{3}-\d{4}\b|\b\d{4}-\d{2}-\d{2}\b|\b\d{2}[a-zA-Z]{3}\d{2}\b|\b\d{1,2}\s[a-zA-Z]{3}\s\d{4}\b|\b\d{2}\s[a-zA-Z]{3}\s\d{2}\b'

    date_regex = re.compile(date_patterns)
    rearranged_list = []
    for text in text_list:
        # Find the first date in the string
        match = date_regex.search(text)
        if match:
            # Extract the date and the rest of the string
            date = match.group()
            rest_of_string = text[:match.start()] + text[match.end():]

            # Rearrange the string with the date at the beginning
            rearranged_text = date + " " + rest_of_string
            rearranged_list.append(rearranged_text)
        else:
            # If no date is found, keep the string as is
            rearranged_list.append(text)

    return rearranged_list

def remove_dates_not_matching_format(lst, date_format):
    # Compile a regex pattern to match potential dates (broadly)
    date_regex = re.compile(r'\b\d{1,2}[-./]\d{1,2}[-./]\d{2,4}\b|\b\d{1,2}\s[a-zA-Z]{3}\s\d{2,4}\b')

    def check_format(date_str, format):
        try:
            datetime.strptime(date_str, format)
            return True
        except ValueError:
            return False

    def process_string(s):
        matches = date_regex.findall(s)
        for match in matches:
            # Remove the date if it doesn't match the format
            if not check_format(match, date_format):
                s = s.replace(match, '')
        return s

    return [process_string(element) for element in lst]

def remove_word_name(s):
    # The pattern matches 'name' in any case (lowercase, uppercase, mixed)
    pattern = r'\b[nameNAME]+\b'
    
    # Replace the word 'name' with an empty string
    return re.sub(pattern, '', s, flags=re.IGNORECASE)

def remove_word_po(s):
    # The pattern matches 'name' in any case (lowercase, uppercase, mixed)
    pattern = r'\b[poPO]+\b'
    
    # Replace the word 'name' with an empty string
    return re.sub(pattern, '', s, flags=re.IGNORECASE)


def extract_name(lst):
    
    Name=[ele for ele in lst if( 'name'  in ele.lower() ) and (':' in ele)]
    if len(Name)>0:
        return [s for s in [remove_word_name(ele).replace(':','').strip() for ele in Name ] if s.isupper()][0]
    
#     elif len([ele.replace('.','') for ele in plain_text_data if( 'p.o.'  in ele.lower() ) ])>0:
#         Name=[ele.replace('.','') for ele in plain_text_data if( 'p.o.'  in ele.lower() ) ]
#         return [ele.lower().split('po')[0].strip() for ele in Name][0]
    else:
        try:
            Name=[s for s in lst if s.isupper() and not any(char.isdigit() for char in s) and len(s) > 4 and not any(word in s.lower() for word in ['account', 'statement', 'branch', 'bank','emirates','aed','currency'])]
            if len(Name)==1:
                return Name[0]
            else:
                return [element for element in Name if len(element) == max(len(e) for e in Name)][0]
        except:
            return None
        
def determine_order(date_list):
    dates = []
    
    date_formats = ["%d/%m/%Y", "%d-%b-%Y", "%Y-%m-%d", "%d%b%y", "%d %b %Y", "%d %b %y", "%d-%m-%Y", "%d-%b-%y"]

    for s in date_list:
        for fmt in date_formats:
            date_pattern = fmt.replace('%d', r'(\d{2})').replace('%b', r'(\w{3})').replace('%Y', r'(\d{4})').replace('%y', r'(\d{2})').replace('%m', r'(\d{2})')
            match = re.search(date_pattern, s)
            if match:
                date_str = match.group()
                try:
                    date = datetime.strptime(date_str, fmt)
                    dates.append(date)
                    break  # Break the inner loop if a date is found
                except ValueError:
                    continue  # Try the next format if the current one fails

    if not dates:
        return "No valid dates found or format mismatch"

    # Checking the order of the dates
    if all(dates[i] <= dates[i + 1] for i in range(len(dates) - 1)):
        return "Ascending"
    elif all(dates[i] >= dates[i + 1] for i in range(len(dates) - 1)):
        return "Descending"
    else:
        return "Not sorted"


def parse_date_from_start(string, date_format):
    date_length = len(datetime.now().strftime(date_format))
    try:
        return datetime.strptime(string[:date_length], date_format)
    except ValueError:
        return None

def sort_list_by_date(lst, date_format, order='Ascending'):
    # Add an index to each element to track its original position
    indexed_lst = [(ele, idx) for idx, ele in enumerate(lst)]

    # Determine the secondary sort key based on the order
    secondary_sort_key = -1 if order == 'Descending' else 1

    # Sort in ascending order by date, then by original index or its reverse based on the order
    filtered_sorted_list = sorted(
        indexed_lst,
        key=lambda x: (parse_date_from_start(x[0], date_format) or datetime.min, secondary_sort_key * x[1])
    )

    # Extract and return only the elements from the sorted list
    return [ele for ele, idx in filtered_sorted_list]


def extract_elements_with_date(lst, date_format):
    extracted_elements = []
    date_pattern = date_format.replace('%d', r'(\d{2})').replace('%m', r'(\d{2})').replace('%Y', r'(\d{4})')

    for s in lst:
        match = re.match(date_pattern, s)
        if match:
            date_str = match.group()
            try:
                # Try parsing the date
                datetime.strptime(date_str, date_format)
                extracted_elements.append(s)
            except ValueError:
                continue  # Skip entries that don't match the format

    return extracted_elements

def extract_liquidity(s):
    # Find all numbers with decimal points
    numbers_with_decimal = re.findall(r'\d+(?:,\d{3})*\.\d+', s)
    
    # Return the last number found, if any
    return numbers_with_decimal[-1] if numbers_with_decimal else None

def filter_elements_with_decimal_digit(lst):

    decimal_number_pattern = re.compile(r'\b\d+\.\d+\b')

    return [s for s in lst if decimal_number_pattern.search(s)]

def extract_date_from_string(string, date_format):
    date_length = len(datetime.now().strftime(date_format))
    for i in range(len(string) - date_length + 1):
        substring = string[i:i + date_length]
        try:
            parsed_date = datetime.strptime(substring, date_format)
            return parsed_date.strftime(date_format)
        except ValueError:
            continue
    return None

def extract_salary(s):
    # Find all numbers with decimal points
    numbers_with_decimal = [ele for ele in re.findall(r'\d+(?:,\d{3})*\.\d+', s) if ele!='0.00']
    
    if len (numbers_with_decimal )==3:
        return numbers_with_decimal[1] 
    
    elif len (numbers_with_decimal )<=2:
        return numbers_with_decimal[0] 
    
    else:
        return ''