var React = require('react');

module.exports = React.createClass({
    render: function() {
       const title = this.props.title;
       return <div className={'page-header'}><h2>{title}</h2></div>
    }
});

