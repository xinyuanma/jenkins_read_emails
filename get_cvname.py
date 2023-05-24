import win32com.client

outlook = win32com.client.Dispatch('outlook.application').GetNamespace("MAPI")
inbox = outlook.Folders('xinyuan.ma@nokia.com').Folders('Inbox')
messages = inbox.Items

for msg in messages:
    if 'Document' in msg.Subject and 'has been' in msg.Subject :
        print(msg.Subject.split()[0]) 
