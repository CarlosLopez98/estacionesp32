from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for, abort
from datetime import datetime


page = Blueprint('page', __name__)


@page.route('/')
def index():

    return render_template('index.html')
