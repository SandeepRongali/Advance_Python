import imaplib
import email
from email.header import decode_header
import os
# import getpass # <-- Removed getpass import

# --- Connection Details (Use environment variables or input - WARNING: input is insecure) ---
IMAP_SERVER = 'imap.gmail.com' # e.g., 'imap.gmail.com'
EMAIL_ACCOUNT = os.environ.get('EMAIL_USER') or input("Enter your email: ")

# --- Password Handling (Removed getpass) ---
# Option 1: Rely *only* on environment variable (more secure than input)
# PASSWORD = os.environ.get('EMAIL_PASS')
# if not PASSWORD:
#     raise ValueError("Email password not found in EMAIL_PASS environment variable.")

# Option 2: Fallback to standard input (INSECURE - password will be visible)
PASSWORD = os.environ.get('EMAIL_PASS') or input("Enter your password (WARNING: WILL BE VISIBLE): ")
# --- End Password Handling ---


# --- Function to decode email headers ---
def decode_str(s, encoding='utf-8'):
    """Decodes a string, handling potential encoding issues."""
    if isinstance(s, bytes):
        try:
            return s.decode(encoding)
        except UnicodeDecodeError:
            try:
                return s.decode('latin-1')
            except UnicodeDecodeError:
                return s.decode('ascii', 'ignore')
    return s

def clean_header(header_value):
    """Decodes email header values properly."""
    if header_value is None:
        return ""
    decoded_parts = decode_header(header_value)
    header_str = ""
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            charset = encoding if encoding else 'utf-8'
            try:
                header_str += part.decode(charset)
            except (UnicodeDecodeError, LookupError):
                try:
                    header_str += part.decode('latin-1')
                except UnicodeDecodeError:
                    header_str += part.decode('ascii', 'ignore')
        else:
            header_str += part
    return header_str

# --- Main Logic ---
mail = None
try:
    # Connect to the server
    print(f"Connecting to {IMAP_SERVER}...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)

    # Login
    print(f"Logging in as {EMAIL_ACCOUNT}...")
    # Check if password was actually obtained
    if not PASSWORD:
        print("Error: Password not provided via environment variable or input.")
        exit()
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    print("Login successful.")

    # Explicitly select the INBOX folder
    status, messages_data = mail.select("INBOX")

    if status != 'OK':
        print(f"Error selecting INBOX: {messages_data}")
        exit()

    print(f"INBOX selected successfully. Total messages: {decode_str(messages_data[0])}")

    # Search for emails within the selected INBOX
    search_criteria = 'ALL'
    print(f"Searching INBOX for emails with criteria: '{search_criteria}'...")
    status, search_data = mail.search(None, search_criteria)

    if status != 'OK':
        print(f"Error searching emails: {search_data}")
        exit()

    email_ids = search_data[0].split()
    print(f"Found {len(email_ids)} emails matching criteria in INBOX.")

    # Fetch and process emails (e.g., fetch the 5 newest)
    num_to_fetch = 5
    for i in range(len(email_ids) -1, max(-1, len(email_ids) -1 - num_to_fetch), -1):
        email_id = email_ids[i]
        print(f"\n--- Fetching email ID: {decode_str(email_id)} ---")
        status, msg_data = mail.fetch(email_id, '(RFC822)')

        if status != 'OK':
            print(f"Error fetching email {decode_str(email_id)}: {msg_data}")
            continue

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = clean_header(msg['subject'])
                from_ = clean_header(msg['from'])
                date_ = clean_header(msg['date'])

                print(f"  From: {from_}")
                print(f"  Subject: {subject}")
                print(f"  Date: {date_}")

finally:
    # Clean up connection
    if mail:
        try:
            mail.close()
            print("Mailbox closed.")
        except imaplib.IMAP4.error as e:
            print(f"Error closing mailbox: {e}")
        mail.logout()
        print("Logged out.")