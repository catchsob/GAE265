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

    # 2. recognize
    r = car.recognize_plate(image, service='service.json')
    print(r)

    # 3. return response
    result = {"plate": r or "未辨識"}

    return result

app.run()