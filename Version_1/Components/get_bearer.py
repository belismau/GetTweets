# My way to get bearer token
def get_bearer():
    with open('API_info/codes.txt', 'r') as f:
        for line in f:
            cur_line = line.split()
            try:
                if cur_line[0][:8] == 'AAAAAAAA':
                    return cur_line[0]
            except:
                pass