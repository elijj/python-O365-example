import click
from O365 import Connection
from O365 import Account


@click.command()
@click.option('--clientid','-id',  help='Azure Application (client) ID', required=1)
@click.option('--secret','-sec', help='Azure Application client secret', required=1)
@click.option('--recepient','-r',  help='Email recepient email', required=1)
@click.option('--subject','-sub',  help='Email subject line' )
@click.option('--body','-b', help='Email body' )
def main(clientid,secret,recepient,subject,body):
    credentials = (clientid,secret)
    scopes = ['https://graph.microsoft.com/Mail.ReadWrite', 'https://graph.microsoft.com/Mail.Send']
    con = Connection(credentials, scopes=scopes)
    account = Account(credentials)
    m = account.new_message()
    m.to.add(recepient)
    m.subject = subject    
    m.body = body
    m.send()

if __name__ == '__main__':
   main()
#main('1637ec5d-1502-45c1-8c01-902d77cbb2b8','knCJ*bC9@ODmx.bRbYs6:PfNuTC5kAz3','eli.jackson@alaskaair.com','test' ,'test')