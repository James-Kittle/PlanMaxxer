from __main__ import app
from flask import jsonify
import json

@app.route('/calendar')
def calendar_route():
    return '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>PlanMaxxer - Calendar</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1; 
    }

    ::-webkit-scrollbar-thumb {
        background: #888; 
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #555; 
    }
    .hour {
    	background-color: #8282ff;
        padding: 0px!important;
        border-radius: 10px;
        box-shadow: 0px 0px 5px 1px #8282ff;
        color: white;
        text-align: center;
        margin-bottom: 10px;
        margin-left: 5px;
        margin-right: 5px;
        min-width: 125px;
    }
    .dayLabel {
    	background-color: #6b6be5;
        border-radius: 10px;
        padding: 1%;
        box-shadow: 0px 0px 5px 1px #8282ff;
        color: white;
        text-align: center;
        margin-bottom: 10px;
        margin-left: 5px;
        margin-right: 5px;
        min-width: 125px;
    }
    .hour img {
    	width: 50%;
    }
    .remove-all-margin {
        margin:0 !important;
        padding:0 !important;
    }
    .break {
  		flex-basis: 100%;
  		height: 0;
	}
    .card-header {
        padding: 0px!important;
    }
    </style>
  </head>
  <body>
    <nav class="navbar" style="background-color: #3bdddb;">
        <div class="container-fluid" >
            <span class="navbar-brand mb-0 h1">PlanMaxxer - Weather</span>
            <a class="nav-link" aria-current="page" href="/">Return Home</a>
        </div>
    </nav>
    <main class="flex-shrink-0 d-flex justify-content-center" style="padding: 1%;">
        <div class="container remove-all-margin">
    <div id="dayModal" class="modal fade" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
            <div class="modal-header">
                <h5 id="modal-date" class="modal-title">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>Example Event</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
            </div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header" style="background-color: #6464e5; color: white;">
            <h4 id="header" class="card-title" style="padding:1%;">Calendar</h4>
        </div>
        <div id="calendar" class="card-body" style="overflow-y: auto;background-color: #a8a8ff;">
            <div id="days" class="row flex-nowrap" id="hourly">
                <div class="col dayLabel" id="hour-template">
                    <h5 id="date">Sunday</h5>
                </div>
                <div class="col dayLabel" id="hour-template">
                    <h5 id="date">Monday</h5>
                </div>
                <div class="col dayLabel" id="hour-template">
                    <h5 id="date">Tuesday</h5>
                </div>
                <div class="col dayLabel" id="hour-template">
                    <h5 id="date">Wednesday</h5>
                </div>
                <div class="col dayLabel" id="hour-template">
                    <h5 id="date">Thursday</h5>
                </div>
                <div class="col dayLabel" id="hour-template">
                    <h5 id="date">Friday</h5>
                </div>
                <div class="col dayLabel" id="hour-template">
                    <h5 id="date">Saturday</h5>
                </div>
            </div>
            <div id="row" class="row flex-nowrap dayrow" id="hourly">
                    <div id="day" class="col card hour" id="hour-template" style="display: none;">
                        <div class="card-header" style="background-color: #6464e5; color: white;">
                            <h4 id="date" class="card-title" style="float: left; display: inline-block;margin-left: 20px;">Calendar</h4>
                            <img data-bs-toggle="modal" data-bs-target="#dayModal" id="expand" src="/static/icons/expand.svg" style="float: right; width: 20%; display: inline-block;">
                        </div>
                        <div class="card-body">
                            <p id="events"><b>Today is clear!</b></p>
                        </div>
                    </div>
            </div>
        </div>
    </div>
    <div style="margin:auto;width:100%;text-align:center;padding-top:20px;">
        <button id="lastmonth" type="button" class="btn btn-primary">&larr; Last Month</button>
        <button id="nextmonth" type="button" class="btn btn-primary">Next Month &rarr;</button>
    </div>
    <div style="margin:auto;width:100%;text-align:center;padding-top:10px;">
        <button id="lastyear" type="button" class="btn btn-primary">&larr; Last Year</button>
        <button id="nextyear" type="button" class="btn btn-primary">Next Year &rarr;</button>
    </div>
    </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="/static/js/calendar.js"></script>
  </body>
</html>
'''