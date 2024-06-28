import sanic
import google.protobuf as pb
import googleplay_pb2 as gp
import gzip
import requests

app = sanic.Sanic(__name__)

@app.get("/")
async def home(request: sanic.Request):
	return sanic.text("GMSEmulator is running",200)


# Authentication stuff
@app.post("/auth")
async def auth(request: sanic.Request):
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
async def checkavail(request: sanic.Request):
	return sanic.json({"status": "SUCCESS"}, 200,{"Server":"GSE","Content-Type":"text/plain; charset=utf-8"})
@app.post("/setup/ratepw")
async def ratepw(request: sanic.Request):
	return sanic.json({"status":"SUCCESS","detail": "Password is strong","strength": 0xFF},200)
@app.post("/setup/create")
async def create_account(request: sanic.Request):
	return sanic.json({"status": "SUCCESS","services": "mail,talk,ig,writely,reader,androidmarket"}, 200)

# Google Play stuff
@app.get("/video/avi/suggest/SuggRequest")
async def suggrequest(request: sanic.Request):
	return sanic.json(["Hello from GMSEmulator!"],200)
@app.get("/proxy/gsasuggest/search")
async def gsasuggest(request: sanic.Request):
	return sanic.json(["Hello from GMSEmulator!"],200)
@app.get("/fdfe/toc")
async def toc(request: sanic.Request):
	# TODO: Try to return different types
	msg = gp.TocResponse(
        	corpus=[
        	    gp.CorpusMetadata(backend=1, name="Corpus1", landingUrl="http://example.com", libraryName="Library1"),
        	    gp.CorpusMetadata(backend=2, name="Corpus2", landingUrl="http://example.org", libraryName="Library2")
        	],
        	tosVersionDeprecated=1,
        	tosContent="Test Content",
        	homeUrl="http://home.example.com",
        	experiments=gp.Experiments(experimentId=[""]),
        	tosCheckboxTextMarketingEmails="Amogus",
        	tosToken="test42",
        	userSettings=gp.UserSettings(tosCheckboxMarketingEmailsOptedIn=False),
        	iconOverrideUrl="http://icon.example.com"
    	)
	return sanic.raw(msg.SerializeToString(),200,content_type="application/x-protobuf")

# Some Google Services Framework stuff
@app.post("/checkin")
async def checkin(request: sanic.Request):
	return sanic.json({},200)

# Google Sync stuff
@app.get("/gsync/sub")
async def gsync_sub(request: sanic.Request):
	return sanic.text("<xml></xml>",200,content_type="text/xml")

# Google Maps stuff
@app.post("/glm/mmap")
def maps_mmap(request: sanic.Request):
	# For now, we'll proxy this
	b = requests.post("https://clients4.google.com/glm/mmap",request.body,headers=request.headers)
	return sanic.raw(b.content,b.status_code,headers=b.headers)
@app.get("/gmm/upgrades/index.html")
async def maps_upgrades_html(request: sanic.Request):
	return sanic.html("<h3>TODO</h3>\n<p>Update bypassing hasen't been implemented yet :(</p>\n<hr><style>body { background: black; color: white; }; hr { background: lightcyan; }</style><script>window.close();</script>")

# Google Chrome Sync stuff
@app.post("/chrome-sync/command")
def chrome_sync_command(request: sanic.Request):
	return sanic.text("",200)

# Google Plus stuff
ApiaryFields = {
	"appVersion": 0,
	"appVersionFull": {},
	"effectiveUser": "true",
	"experimentOverride": "",
	"noLog": False,
	"socialClient": {},
	"socialClientString": "",
	"sourceInfo": "",
}
@app.post("/plusi/v2/ozInternal/getmobilesettings")
def plusi_getmobilesettings(request: sanic.Request):
	return sanic.json({"allowNonGooglePlusUsers": True, "commonFields": ApiaryFields,"enableTracing": False, "fbsVersionInfo": "0.0"},200)

if __name__ == "__main__":
	app.run(port=8095,dev=True)