# author = rhnvrm <hello@rohanverma.net>
import os
from flask import Flask, request, render_template, jsonify
from twitter import TwitterClient

app = Flask(__name__)
# Setup the client <query string, only_retweets bool>
api = TwitterClient('@Sirajology', False)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/tweets')
def tweets():
        only_retweets = request.args.get('only_retweets')
        if(only_retweets == 'false'):
            api.set_retweet_checking(False)
        else:
            api.set_retweet_checking(True)
        tweets = api.get_tweets()
        return jsonify({'data': [{'text': t.text, 'name': t.user.screen_name}
                        for t in tweets], 'count': len(tweets)})


port = int(os.environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=port, debug=True)
