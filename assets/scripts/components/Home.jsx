import React, { Component } from 'react';
import PropTypes from 'prop-types';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';


export default class Home extends Component {

  static propTypes = {
    onJoinRoom: PropTypes.func
  };

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="home">
        <TextField
          hintText="Hint Text"
          floatingLabelText="Floating Label Text"
        />
        <RaisedButton
          label="Join Room"
          primary={true}
          onClick={this.props.onJoinRoom}
        />
      </div>
    );
  }

}
