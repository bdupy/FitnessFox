from sqlalchemy import Column, Integer, String
from fitness_fox import db


class Workout(db.Model):
	__tablename__ = 'Workout'

	id = db.Column(db.Integer, primary_key=True)
	activityDb = db.Column(db.String(50), unique=False)
	dateDb = db.Column(db.Date, nullable=True)
	timeDb = db.Column(db.Time, nullable=True)
	minutesDb  = db.Column(db.Integer)

	def __init__(self, activityDb, activity_date, activity_time,activity_mins):
		self.activityDb = activityDb
		self.dateDb = activity_date
		self.timeDb = activity_time
		self.minutesDb = activity_mins