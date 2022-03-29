from sparkpost import SparkPost

sp = SparkPost('809b8f60d5c49139222e0b9ff8b7bacac72363e1')

try:
	sp.transmissions.send(
	    recipients=['javipkr@gmail.com'],
	    html='<p>Bienvenido al campus! Tu registro se ha completado satisfactoriamente</p>',
	    from_email='test@urideveloper.eu',
	    subject='Hello from python-sparkpost'
)

except SparkPostAPIException as err:
    # http response status code
    print(err.status)
    # python requests library response object
    # http://docs.python-requests.org/en/master/api/#requests.Response
    print(err.response.json())
    # list of formatted errors
    print(err.errors)



