var React = require('react');
var ReactDOM = require('react-dom');
var Bootstrap = require('react-bootstrap');

var App = require('./app');


require('bootstrap/dist/css/bootstrap.css');

// require('bootstrap/dist/css/bootstrap.css');
// var common = require('./common');

require("../../sass/main.scss");

ReactDOM.render(<App/>, document.querySelector('.container'));
// ReactDOM.render(<App/>, document.getElementById('content'));
