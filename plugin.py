def results(fields, original_query):
    message = fields['~message']
    log(message)
    return {
        "title": "ab '{0}'".format(message),
        "run_args": [message]
    }


def run(message):
    log(message)

def log(message):
    file = open('/Users/Xu/ab.log', 'x')
    file.write(message)
    file.close()
