import sanic
import google.protobuf as pb
import googleplay_pb2 as gp

app = sanic.Sanic(__name__)

@app.get("/")
def home(request: sanic.Request):
	return sanic.text("GMSEmulator is running",200)

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

@app.get("/fdfe/toc")
def toc(request: sanic.Request):
	# TODO: Try to return different types
	msg = gp.AppDetails()
	msg.title = "Haiiyaa"
	msg.appType = "Free"
	return sanic.text(msg.SerializeToString().decode("latin8"),200)

@app.get("/video/avi/suggest/SuggRequest")
def suggest(request: sanic.Request):
	return sanic.json([],200)

# Google sync

@app.get("/gsync/sub")
def gsync_sub(request: sanic.Request):
	return sanic.text("",200)

if __name__ == "__main__":
	app.run(port=8095,dev=True)