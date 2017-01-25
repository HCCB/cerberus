var React = require('react');

var Section = require('./section');

var SampleLabel = React.createClass({
    render: function() {
        const labelText = this.props.labelText;
        const classes = classNames("label", this.props.labelClass);
        return <span className={classes}>{labelText}</span> 
    }
});

var SampleLabels = React.createClass({
    render: function () {
        const tableClass = this.props.tableClass
    }
});

module.exports = React.createClass({
    genLabels: function() {
      return [
             <SampleLabel labelClass="label-default" labelName="Default"/>,
             <SampleLabel labelClass="label-primary" labelName="Primary"/>,
             <SampleLabel labelClass="label-success" labelName="Success"/>,
             <SampleLabel labelClass="label-info" labelName="Info"/>,
             <SampleLabel labelClass="label-warning" labelName="Warning"/>,
             <SampleLabel labelClass="label-danger" labelName="Danger"/>
             ]
    },
    render: function() {
       return <div>
		<Section title="Labels"/>
		<h1>{ genLabels() }</h1>
              </div>
    }
});

