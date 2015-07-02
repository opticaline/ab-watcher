# -*- coding: utf-8 -*-


def results(fields, original_query):
    message = fields['~message']
    return {
        "title": "Say '{0}'".format(message),
        "run_args": [message],
        "html": """
		<div style='font-family: sans-serif; padding: 2em'>
			<h1>{0}</h1>
			<p><a href='flashlight://plugin/say-with-settings/preferences'>Open Settings</a></p>
		</div>
		""".format(message)
    }


def run(message):
    pass
