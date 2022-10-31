from flask import Flask, flash, request, render_template

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

proteins = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M','ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_','TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}



@app.route("/", methods = ["POST", "GET"])
def default():
	return render_template("home.html")
	

@app.route("/translate", methods = ["POST", "GET"])
def translate():
	seq = ""
	if request.method == "POST":
		data = request.form.get("translate-input-name")
		data0 = str(data)
		data0 = data0.upper()
		for i in range(0, len(data0), 3):
			if(data0[i:i+3]):
				seq += proteins[data0[i:i+3]]
		if len(data0)%3==0:
			flash(seq)
			return render_template("home.html")
		elif len(data0)%3!=0:
			flash("Sequence is not divisible by 3")
			return render_template("home.html")
	else:
		flash("please enter one")
		return render_template("home.html")


if __name__ == "__main__":
	app.run()