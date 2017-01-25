var React = require('react');

var Section = require('./section');

module.exports = React.createClass({
    render: function() {
       return <div>
		<Section title="Buttons"/>
      <p>
        <button type="button" className="btn btn-lg btn-default">Default</button>
        <button type="button" className="btn btn-lg btn-primary">Primary</button>
        <button type="button" className="btn btn-lg btn-success">Success</button>
        <button type="button" className="btn btn-lg btn-info">Info</button>
        <button type="button" className="btn btn-lg btn-warning">Warning</button>
        <button type="button" className="btn btn-lg btn-danger">Danger</button>
        <button type="button" className="btn btn-lg btn-link">Link</button>
      </p>
      <p>
        <button type="button" className="btn btn-default">Default</button>
        <button type="button" className="btn btn-primary">Primary</button>
        <button type="button" className="btn btn-success">Success</button>
        <button type="button" className="btn btn-info">Info</button>
        <button type="button" className="btn btn-warning">Warning</button>
        <button type="button" className="btn btn-danger">Danger</button>
        <button type="button" className="btn btn-link">Link</button>
      </p>
      <p>
        <button type="button" className="btn btn-sm btn-default">Default</button>
        <button type="button" className="btn btn-sm btn-primary">Primary</button>
        <button type="button" className="btn btn-sm btn-success">Success</button>
        <button type="button" className="btn btn-sm btn-info">Info</button>
        <button type="button" className="btn btn-sm btn-warning">Warning</button>
        <button type="button" className="btn btn-sm btn-danger">Danger</button>
        <button type="button" className="btn btn-sm btn-link">Link</button>
      </p>
      <p>
        <button type="button" className="btn btn-xs btn-default">Default</button>
        <button type="button" className="btn btn-xs btn-primary">Primary</button>
        <button type="button" className="btn btn-xs btn-success">Success</button>
        <button type="button" className="btn btn-xs btn-info">Info</button>
        <button type="button" className="btn btn-xs btn-warning">Warning</button>
        <button type="button" className="btn btn-xs btn-danger">Danger</button>
        <button type="button" className="btn btn-xs btn-link">Link</button>
      </p>
              </div>
    }
});

