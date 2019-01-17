class Company:
    def __init__(self, account_info, subs=[], token=''):
        self.account_info = account_info
        self.subs = subs
        self.token = token
info = {'whulme':'aaroniscute'}
s = [{'asdfasd;jlk':'asdfasdf'},
    {'adsfsd':'sdadasf'},
    ]
t = 'aaroniscute'
cocacola = Company(account_info=info, subs=s, token=t)

print(cocacola.account_info)
print(cocacola.subs)