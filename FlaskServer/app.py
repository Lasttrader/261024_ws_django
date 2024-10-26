import pickle

from joblib.parallel import method
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

from flask import Flask, jsonify, request

app = Flask(__name__)

#load_models
#le
job_LE = pickle.load(open('../FlaskServer/models/job_LE.pkl', 'rb'))
marital_LE = pickle.load(open('../FlaskServer/models/marital_LE.pkl', 'rb'))
education_LE = pickle.load(open('../FlaskServer/models/education_LE.pkl', 'rb'))
default_LE = pickle.load(open('../FlaskServer/models/default_LE.pkl', 'rb'))
housing_LE = pickle.load(open('../FlaskServer/models/housing_LE.pkl', 'rb'))
loan_LE	= pickle.load(open('../FlaskServer/models/loan_LE.pkl', 'rb'))
contact_LE	= pickle.load(open('../FlaskServer/models/contact_LE.pkl', 'rb'))
month_LE	= pickle.load(open('../FlaskServer/models/month_LE.pkl', 'rb'))
poutcome_LE	= pickle.load(open('../FlaskServer/models/poutcome_LE.pkl', 'rb'))
#predict le
y_LE = pickle.load(open('../FlaskServer/models/y_LE.pkl', 'rb'))
#scaler
num_scaler = pickle.load(open('../FlaskServer/models/num_scaler.pkl', 'rb'))
#ML models
kNN = pickle.load(open('../FlaskServer/models/kNN.pkl', 'rb'))

#get_data


def predict(client_data) -> str:
    """
    Прогноз

    :return: Результат yes/no
    """
    ##categorical
    X_cat_from_keyboard = client_data[0][0:9]
    print(X_cat_from_keyboard)
    # print(X_cat_from_keyboard)
    le_list = [job_LE,
               marital_LE,
               education_LE,
               default_LE,
               housing_LE,
               loan_LE,
               contact_LE,
               month_LE,
               poutcome_LE]
    X_le_list = [] #под закодированные признаки
    for i in range(len(X_cat_from_keyboard)):
        x_cat = le_list[i].transform([X_cat_from_keyboard[i]])[0]
        # print(x_cat)
        X_le_list.append(x_cat)
    print('X_cat_le:', X_le_list)
    ##num

    X_nums_from_keyboard = client_data[0][9:]
    print('X_nums', X_nums_from_keyboard)
    #объединить категориальные и числовые (в том же порядке, как и при обучении)
    X = []
    X.extend(X_le_list)
    X.extend(X_nums_from_keyboard)
    print('X:', X)
    #scaler
    X_scaled = num_scaler.transform([X])
    print('X_scaled:', X_scaled)
    #predict
    prediction = kNN.predict(X_scaled)
    print(prediction)
    #result
    result = y_LE.inverse_transform(prediction)[0]
    return result

@app.route("/api/v1/get_data/", methods=["GET", "POST"])
def get_data():
    client_data = request.json['client_form'] #получаем json от клиента

    return jsonify({'result': predict(client_data)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
