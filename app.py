from flask import Flask,render_template,request,redirect,url_for
from backend.main import fazer_video
from backend.uploads_plataforms import upload_to_tiktok

app = Flask(__name__)
resposta = ''

@app.route('/success')
def sucessPage():
    return render_template('sucessPage.html',resposta=resposta)

@app.route('/')
def homepage():

    if 'script' in request.url and request.args.get('script') != '' and len(request.args.get('script')) > 0:
        #resposta = fazer_video(request.args.get('script'))
        if 'tiktok' in request.url and 'youtube' in request.url:
            resposta = 'tiktok e youtube'

        if 'youtube' in request.url and not 'tiktok' in request.url:
            resposta = 'youtube mermao'

        if 'tiktok' in request.url and not 'youtube' in request.url:
            resposta = fazer_video(request.args.get('script'))
            #upload_to_tiktok()
            return redirect(url_for('sucessPage'),200)

    return render_template('homepage.html')

if __name__ == '__main__':
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True,
        FLASK_DEBUG=1
    )
    app.run(debug=True,use_reloader=True)
