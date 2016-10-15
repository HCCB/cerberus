var React = require('react');
var ReactDOM = require('react-dom');
var App = require('./app');

// require("bootstrap/dist/css/bootstrap.min.css");
// require("bootstrap/dist/css/bootstrap-theme.min.css");

// require("../css/style.css");
require("../sass/main.scss");

ReactDOM.render(<App/>, document.getElementById('content'));
