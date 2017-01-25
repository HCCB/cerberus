var React = require('react');

var Section = require('./section');
var Placeholder = require('react-placeholder');

module.exports = React.createClass({
    render: function() {
       return <div>
		<Section title="Thumbnails"/>
      <img data-src="holder.js/200x200" class="img-thumbnail" alt="A generic square placeholder image with a white border around it, making it resemble a photograph taken with an old instant camera">

              </div>
    }
});

