from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Han19981130..@localhost:3306/collections'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Anthropology(db.Model):
    __tablename__ = 'Anthropology'
    AccessionNumber = db.Column(db.String(255), unique=True, primary_key=True)
    ObjectName = db.Column(db.String(255))
    Description = db.Column(db.TEXT)
    Height = db.Column(db.String(255))
    Width = db.Column(db.String(255))
    Materials = db.Column(db.String(255))
    Site = db.Column(db.String(255))
    Acquisition = db.Column(db.String(255))
    LatestDate = db.Column(db.String(255))
    ImgUrl = db.Column(db.String(255))


# class Archery(db.Model):
#     __tablename__ = 'Archery'
#     AccessionNumber = db.Column(db.String(256), unique=True, primary_key=True)
#     ObjectName = db.Column(db.String(256))
#     Description = db.Column(db.TEXT)
#     Height = db.Column(db.String(256))
#     Width = db.Column(db.String(256))
#     Materials = db.Column(db.String(256))
#     Site = db.Column(db.String(256))
#     Acquisition = db.Column(db.String(256))
#     LatestDate = db.Column(db.String(256))
#     ImgUrl = db.Column(db.String(256))
#
#
# class Egyptology(db.Model):
#     __tablename__ = 'Egyptology'
#     AccessionNumber = db.Column(db.String(256), unique=True, primary_key=True)
#     ObjectName = db.Column(db.String(256))
#     Description = db.Column(db.TEXT)
#     Height = db.Column(db.String(256))
#     Width = db.Column(db.String(256))
#     Materials = db.Column(db.String(256))
#     Site = db.Column(db.String(256))
#     Acquisition = db.Column(db.String(256))
#     LatestDate = db.Column(db.String(256))
#     ImgUrl = db.Column(db.String(256))


# if __name__ == '__main__':
#     db.drop_all()
#     db.create_all()
#
#     cl1 = Anthropology(AccessionNumber='0.9707/142.d', ObjectName='Vessel', Description='Small fragment of vessel')
#     db.session.add_all(cl1)
#     db.session.commit()
#
#     app.run(port=8888)