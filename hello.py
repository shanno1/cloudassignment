import os 
from flask import Flask, jsonify
app = new Flask(__name__)

Entries = [
	{
		'id':1,
		'Date':u"29/07/2014",
		'Start_time':u"13:00",
		'End_time':u"16:00",
		'Repeats':u'None',
		'Location':u'https://www.google.ie/maps/place/DIT-Kevin+Street/@53.3372301,-6.2684233,17z/data=!3m1!4b1!4m2!3m1!1s0x48670c2089d84a1d:0x6e1d03e3d62489ae'
	}
]

@app.route('/todo/api/v1.0/Entries', methods = ['GET'])
def get_Entries():
	Entry = filter(lambda t: t['id'] == id, Entries)
	if len(Entry) == 0:
		abort(404)

	return jsonify( { 'Entries': Entries } )



@app.route('/todo/api/v1.0/Entries', methods = ['POST'])
def create_Entry():
	if not request.json or not 'title' in request.json:
		abort(400)
	Entry = {
		'id': Entries[-1]['id'] + 1,
		'title': request.json['title'],
		'Date': request.json['Date'],		
		'Start_time': request.json['Start_time'],
		'End_time': request.json['End_time'],
		'Repeats': request.json['Repeats'],
		'Location': request.json.get('Location',"")


	}

	Entries.append(Entry)
	return jsonify( { 'Entry': Entry } ), 201



def update_Entry(id):
	Entry = filter(lambda t: t['id'] == id, Entries)
	if len(Entry) == 0:
        	abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != unicode:
		abort(400)
	if 'Date' in request.json and type(request.json['Date']) != unicode:
                abort(400)
	if 'Start_time' in request.json and type(request.json['Start_time']) != unicode:
                abort(400)
	if 'End_time' in request.json and type(request.json['End_time']) != unicode:
                abort(400)
	if 'Repeats' in request.json and type(request.json['Repeats']) != unicode:
                abort(400)
	if 'Location' in request.json and type(request.json['Location']) != unicode:
                abort(400)

	Entry[0]['title'] = request.json.get('title', Entry[0]['title'])
	Entry[0]['Date'] = request.json.get('Date', Entry[0]['Date'])
	Entry[0]['Start_time'] = request.json.get('Start_time', Entry[0]['Start_time'])
	Entry[0]['End_time'] = request.json.get('End_time', Entry[0]['End_time'])	
	Entry[0]['Repeats'] = request.json.get('Repeats', Entry[0]['Repeats'])
	Entry[0]['Location'] = request.json.get('Location', Entry[0]['Location'])

	return jsonify( { 'Entry': Entry[0] } )

@app.route('/todo/api/v1.0/Entries/<int:id>', methods = ['DELETE'])
def delete_Entry(id):
	Entry = filter(lambda t: t['id'] == id, Entries)
	if len(Entry) == 0:
		abort(404)
	Entries.remove(Entry[0])
	return jsonify( { 'result': True } )
   
if __name__ = '__main__':
	app.run()
