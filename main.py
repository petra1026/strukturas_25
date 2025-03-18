from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # random joks
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = response.json()

    # kategorijas
    response = requests.get("https://api.chucknorris.io/jokes/categories")
    categories = response.json()

    # search un kategorijas
    if request.method == "POST":
        if "meklet" in request.form:
            query = request.form["meklet"]
            response = requests.get(f"https://api.chucknorris.io/jokes/search?query={query}")
            results = response.json()
            if "result" in results:
                return render_template(
                    "index.html", 
                    meklesanas_rezultati=results["result"][:5],
                    kategorijas=categories
                )

        elif "kat" in request.form:
            category = request.form["kat"]
            response = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
            joke = response.json()

    return render_template(
        "index.html",
        joks=joke["value"],
        bilde=joke["icon_url"],
        kategorijas=categories
    )

@app.route("/uni")
def uni():
    nosaukumi = [
        {
            "nosaukums": "Latvijas Universitāte",
            "majaslapas": ["https://www.lu.lv"]
        },
        {
            "nosaukums": "Rīgas Tehniskā universitāte",
            "majaslapas": ["https://www.rtu.lv"]
        },
        {
            "nosaukums": "Latvijas Lauksaimniecības universitāte",
            "majaslapas": ["https://www.llu.lv"]
        },
        {
            "nosaukums": "Rīgas Stradiņa universitāte",
            "majaslapas": ["https://www.rsu.lv"]
        },
        {
            "nosaukums": "Transporta un sakaru institūts",
            "majaslapas": ["https://www.tsi.lv"]
        }
    ]
    return render_template("universitates.html", uni=nosaukumi)

@app.route("/vardi", methods=["GET", "POST"])
def vardi():
    rezultats = None
    if request.method == "POST" and "teksts" in request.form:
        teksts = request.form["teksts"].strip()
        if teksts:
            with open("teksta_vardu_skaititajs/teksts.txt", "w", encoding="utf-8") as f:
                f.write(teksts)
            
            vardi = teksts.split()
            visi_vardi = {}
            for vards in vardi:
                vards = vards.strip(".,!-?*'\")(").lower()
                if vards:
                    if vards in visi_vardi:
                        visi_vardi[vards] += 1
                    else:
                        visi_vardi[vards] = 1
            rezultats = visi_vardi
            
    return render_template("vardi.html", rezultats=rezultats)

@app.route("/jschats")
def chats():
    return render_template("chats.html")

@app.route("/jschats/suutiit", methods=["POST"])
def suutiit():
    sanemtais = request.json
    if sanemtais["saturs"] == "\\clear":
        with open("chataZinas.txt", "w", encoding="utf-8") as f:
            f.write("")
        return "Izdzests"
    
    with open("chataZinas.txt", "a", encoding="utf-8") as f:
        f.write(sanemtais["vards"])
        f.write("----")
        f.write(sanemtais["saturs"])
        f.write("\n")
    return "OK"

@app.route("/jschats/lasiit")
def lasit():
    saturs = []
    with open("chataZinas.txt", "r", encoding="utf-8") as f:
        saturs = f.readlines()
    return saturs

if __name__ == "__main__":
    app.run(debug=True)