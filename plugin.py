from utils import main

def results(fields, original_query):
    message = fields['~message']
    out = main.video_list([message])
    return {
        "title": "Say '{0}'".format(message),
        "run_args": [out[0]],
        "html": "{0}".format(out)
    }


def run(message):
    main.play_video(message)
