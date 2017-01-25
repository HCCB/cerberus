var React = require('react');
var MyJumbotron = require('./jumbotron');
var MyHeading = require('./headings');
var MyButtons = require('./buttons');
var MyTables = require('./tables');
var MyLabels = require ('./labels');

module.exports = React.createClass({
     render: function() {
         return <div>
                    <MyLabels/>
                </div>
     }
});
