from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.app_context().push()

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "{} {} {}".format(self.id, self.name, self.email)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

db.create_all()

@app.route("/")
def home():
    return jsonify({'result': 'success', 'message': "Flask works!"})

@app.route("/api/v1.0/contacts")
def contacts():
    result = Contact.query.all()
    contacts = list(map(lambda c : c.serialize(), result))
    return jsonify({'result': 'success', 'contacts': contacts})

@app.route("/api/v1.0/contact", methods=['GET'])
def contact_get():
    data = request.json
    cid = data.get('cid')
    contact = Contact.query.get(cid)
    if contact is None:
        return jsonify({'result': 'error', 'message': 'contact not found'})
    else:
        return jsonify({'result': 'success', 'contact': contact.serialize()})
    

@app.route("/api/v1.0/contact", methods=['POST'])
def contact_post():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    # here it would be good to verify and sanitize data
    contact = Contact(name, email)
    db.session.add(contact)
    db.session.commit()
    return jsonify({'result': 'success', 'contact': contact.serialize()})

@app.route("/api/v1.0/contact", methods=['PUT'])
def contact_put():
    data = request.json
    cid = data.get("cid")
    contact = Contact.query.get(cid)
    if contact is None:
        return jsonify({'result': 'error', 'message': 'contact not found'})
    else:
        # here it would be good to verify and sanitize data
        contact.name = data.get('name')
        contact.email = data.get('email')
        db.session.commit()
        return jsonify({'result': 'success', 'contact': contact.serialize()})

@app.route("/api/v1.0/contact", methods=['DELETE'])
def contact_delete():
    data = request.json
    cid = data.get("cid")
    contact = Contact.query.get(cid)
    if contact is None:
        return jsonify({'result': 'error', 'message': 'contact not found'})
    else: 
        Contact.query.filter_by(id=cid).delete()
        db.session.commit()
        return jsonify({'result': 'success', 'message': 'contact deleted'})
