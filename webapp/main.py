from transcriptapi import *
from flask import *

# initializing flask app
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hit /api with video link in parameter v to get transcript of a video'


@app.route('/api', methods=['GET'])
def api():
    video_link = request.args.get('v')
    return jsonify(get_subtitles(video_link))

 
app.run(debug=True) 
#app.run()