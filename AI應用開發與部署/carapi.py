import flask
import car


app = flask.Flask(__name__)


@app.route('/plate', methods=['POST'])
def recognize():
    # 1. get image and parameters
    files = flask.request.files
    if not files:
        return 'Bad Request', 400
    
    file = files.get('image')
    if not file:
        return 'Bad Request', 400
    
    image = file.stream.read()

    user_id = None
    if flask.request.form:
        user_id = flask.request.form.get('user_id')
    
    model = 'gemini-3.5-flash-lite'
    if flask.request.form:
        model = flask.request.form.get('model', 'gemini-3.5-flash-lite')

    # 2. recognize
    r = car.recognize_plate(image, model=model, service='service.json')
    print(r)

    # 3. return response
    result = {
        "plate": r or "未辨識",
        "model": model,
        "user_id": user_id or "沒有id"
    }

    return result

if __name__ == '__main__':
    app.run()