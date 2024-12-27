from flask import Blueprint, render_template, request, redirect, session

lab9 = Blueprint('lab9', __name__)
def main():
     return render_template('lab9/lab9.html')