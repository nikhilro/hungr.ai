import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Video from './Video';
import { Button } from 'react-bootstrap';

export default class Game extends Component {

  static propTypes = {

  };

  constructor(props) {
    super(props);

    this.state = {

    };
  }

  render() {
    return (
      <div className="game">
        <div className="video-wrapper">
          <Video />
        </div>
        <div>
          <Button bsStyle="primary" bsSize="large" block>Chomp!</Button>
        </div>
      </div>
    );
  }

}
