
from website import create_app
from  website import views

new_data = views.home

app = create_app()

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port= 5000)
