var React = require('react');
var ReactDOM = require('react-dom');
var App = require('./app');

// var common = require('./common');

// require("bootstrap/dist/css/bootstrap.min.css");
// require("bootstrap/dist/css/bootstrap-theme.min.css");

// require("../css/style.css");
// require("bootstrap-loader");

require("../../sass/main.scss");
// require("bootstrap-loader");

ReactDOM.render(<App/>, document.getElementById('content'));
