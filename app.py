import sanic

app = sanic.Sanic(__name__)

@app.post("/auth")
def auth(request: sanic.Request):
	print(request.form)
	return sanic.text(f'''SID=BAD_COOKIE
LSID=BAD_COOKIE
Auth=DQQQQFAKELOGIN==
services=mail,talk,ig,writely,reader,androidmarket
Email={request.form["Email"][0]}
GooglePlusUpgrade=0
firstName=Test
lastName=User''', 200,{"Server":"GSE","Content-Type":"text/plain; charset=utf-8"})

if __name__ == "__main__":
	app.run(port=8095,dev=True)