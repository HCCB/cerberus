var React = require('react');

var MyJumbotron = require('react-bootstrap/lib/Jumbotron');

module.exports = React.createClass({
    render: function() {
        return <MyJumbotron><h1>Hello, there</h1><p>Thi is a  sample Jumbotron</p></MyJumbotron>
    }
});
