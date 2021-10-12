import pandas as pd
import tablefill
import email_listener

EMAIL = "JDstablefiller@gmail.com"
PASSWORD = "qNLcY09KVfcCX56GD289"
NAME = "Table Filler"


def process_attachment(attachment):
    df = pd.read_excel(attachment,
                       dtype=str,
                       index_col=0,
                       header=0)
    print(df)
    df, urls = tablefill.search_whole_table(df)
    df.to_excel('output.xlsx')
    with open('urls.txt', 'w') as u:
        u.write('\n'.join(urls))
    output = {'attachments': ['output.xlsx', 'urls.txt'],
              }
    return output


folder = "Inbox"
attachment_dir = "attachments"
listener = email_listener.EmailListener(EMAIL, PASSWORD, folder, attachment_dir=attachment_dir)
responder = email_listener.email_responder.EmailResponder(EMAIL, PASSWORD)
listener.login()
responder.login()


def process_func(e, f):
    for i in f.keys():
        sender = ''.join(i.split('_')[1:])
        d = f[i]
        file = d['attachments'][0]
        output = process_attachment(file)
        responder.send_multipart_msg(sender,
                                     f"Response from {NAME}",
                                     "Your output is attached",
                                     **output
                                     )


listener.listen(1, process_func=process_func)
