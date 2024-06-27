import sanic
import google.protobuf as pb
import googleplay_pb2 as gp

app = sanic.Sanic(__name__)

@app.get("/")
def home(request: sanic.Request):
	return sanic.text("GMSEmulator is running",200)


# Authentication stuff
@app.post("/auth")
def auth(request: sanic.Request):
	print(request.form)
	return sanic.text(f'''SID=SID
LSID=LSID
Auth=DQQQQFAKELOGIN==
services=mail,talk,ig,writely,reader,androidmarket
Email={request.form["Email"][0]}
GooglePlusUpgrade=1
firstName=Test
lastName=User''', 200,{"Server":"GSE","Content-Type":"text/plain; charset=utf-8"})
# Signing up stuff
@app.post("/setup/checkavail")
def checkavail(request: sanic.Request):
	print(request.form)
	return sanic.json({"status": "SUCCESS"}, 200,{"Server":"GSE","Content-Type":"text/plain; charset=utf-8"})
@app.post("/setup/ratepw")
def ratepw(request: sanic.Request):
	return sanic.json({"status":"SUCCESS","detail": "Password is strong","strength": 0xFF},200)
@app.post("/setup/create")
def create_account(request: sanic.Request):
	return sanic.json({"status": "SUCCESS","services": "mail,talk,ig,writely,reader,androidmarket"}, 200)

# Google Play stuff
@app.get("/video/avi/suggest/SuggRequest")
def suggest(request: sanic.Request):
	return sanic.json([],200)
@app.get("/fdfe/toc")
def toc(request: sanic.Request):
	# TODO: Try to return different types
	msg = gp.AppDetails()
	msg.title = "Haiiyaa"
	msg.appType = "Free"
	return sanic.text(msg.SerializeToString().decode("latin8"),200)

# Google Sync stuff
@app.get("/gsync/sub")
def gsync_sub(request: sanic.Request):
	return sanic.text("",200)

if __name__ == "__main__":
	app.run(port=8095,dev=True)