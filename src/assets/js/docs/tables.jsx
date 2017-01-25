var React = require('react');

var Section = require('./section');

var SampleTable = React.createClass({
    render: function () {
        const tableClass = this.props.tableClass
        return <div className="col-md-6">
          <table className={tableClass}>
            <thead>
              <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
              </tr>
              <tr>
                <td>2</td>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
              </tr>
              <tr>
                <td>3</td>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
              </tr>
            </tbody>
          </table>
        </div>
    }
});

module.exports = React.createClass({
    render: function() {
       return <div>
		<Section title="Tables"/>
		<div className="row">
                    <SampleTable tableClass="table"/>
                    <SampleTable tableClass="table table-striped"/>
		</div>
                <div className="row">
                    <SampleTable tableClass="table table-bordered"/>
                    <SampleTable tableClass="table table-condensed"/>
                </div>
              </div>
    }
});

