var React = require ('react');
var Jumbotron = require('react-bootstrap/lib/Jumbotron');


module.exports = React.createClass({
     render: function() {
          return <Jumbotron> 
                     <h1>Styleguide</h1> 
                     <p> 
                         This is a style guide showcasing Bootstrap and 
                         common HTML elememts, which are displayed on a 
                         single page.  It is a modified version of 
                         Bootstrap 3 theme example.  
                     </p> 
                 </Jumbotron>
     }
});
