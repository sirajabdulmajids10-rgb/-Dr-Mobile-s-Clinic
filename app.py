 from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Dr. Mobile’s Clinic</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">

<style>
body {
    margin:0;
    font-family:'Poppins',sans-serif;
    background:#0b0f19;
    color:white;
}

/* NAVBAR */
.nav {
    display:flex;
    justify-content:space-between;
    padding:15px 20px;
    background:rgba(0,0,0,0.6);
    position:sticky;
    top:0;
}
.nav a {color:white;text-decoration:none;margin:0 10px;}

/* HERO */
.hero {
    padding:60px 20px;
    text-align:center;
    background:linear-gradient(135deg,#0d47a1,#d32f2f);
}
.hero img {
    width:90%;
    max-width:500px;
    border-radius:12px;
    margin-bottom:20px;
}

/* BUTTONS */
.btn {
    display:inline-block;
    margin:10px;
    padding:12px 20px;
    border-radius:30px;
    text-decoration:none;
    font-weight:500;
}
.call {background:white;color:#d32f2f;}
.whatsapp {background:#25D366;color:white;}

/* SECTIONS */
.section {padding:40px 20px;text-align:center;}

.grid {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
    gap:15px;
}

.card {
    background:rgba(255,255,255,0.05);
    padding:20px;
    border-radius:12px;
    backdrop-filter:blur(10px);
    transition:0.3s;
}
.card:hover {transform:scale(1.05);}

/* FLOAT BUTTON */
.float {
    position:fixed;
    bottom:20px;
    right:20px;
    background:#25D366;
    color:white;
    padding:15px;
    border-radius:50%;
    text-decoration:none;
    font-size:20px;
}

/* MAP */
iframe {width:100%;border:0;height:250px;border-radius:10px;}
</style>

</head>

<body>

<div class="nav">
<b>Dr.Mobile</b>
<div>
<a href="#">Home</a>
<a href="#">Services</a>
<a href="#">Contact</a>
</div>
</div>

<div class="hero">
<img src="https://via.placeholder.com/500x200.png?text=Dr+Mobile+Banner">
<h1>Dr. Mobile’s Clinic</h1>
<p>Premium Mobile Repair & Service</p>

<a href="tel:7010861125" class="btn call">📞 Call</a>
<a href="https://wa.me/917010861125" class="btn whatsapp">💬 WhatsApp</a>
</div>

<div class="section">
<h2>Services</h2>
<div class="grid">
<div class="card">📱 Display Repair</div>
<div class="card">🔋 Battery Replace</div>
<div class="card">🧠 Chip Repair</div>
<div class="card">⚙ Full Service</div>
<div class="card">💧 Water Damage</div>
<div class="card">🔌 Charging Issue</div>
</div>
</div>

<div class="section">
<h2>Why Choose Us</h2>
<p>⚡ Fast Service</p>
<p>💰 Best Price</p>
<p>👨‍🔧 Expert Technicians</p>
</div>

<div class="section">
<h2>Location</h2>
<iframe src="https://maps.google.com/maps?q=Mangadu%20Chennai&t=&z=13&ie=UTF8&iwloc=&output=embed"></iframe>
</div>

<a href="https://wa.me/917010861125" class="float">💬</a>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
