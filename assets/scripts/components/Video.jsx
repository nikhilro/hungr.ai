import React, { Component } from 'react';
import PropTypes from 'prop-types';
import openSocket from 'socket.io-client';

const socket = openSocket('http://localhost:8000');


export default class Video extends Component {
  static propTypes = {
    data: PropTypes.string
  };

  constructor(props) {
    super(props);

    this.state = {
      'data': ""
    }

    socket.on('connect', function() {
        console.log('Socket connected!');
        socket.send('read_camera');
    });

    socket.on('videoStart', function(messageEvent) {
      const video = document.querySelector('#video');
      let enc = new TextDecoder("utf-8");
      const data = enc.decode(messageEvent.data);

      this.setState({
        'data': "data:image/jpeg;base64," + data
      });
    });
  }

  render() {
    return (
      <div className="video">
        <img id="video" src={this.props.data}></img>
      </div>
    );
  }
}
