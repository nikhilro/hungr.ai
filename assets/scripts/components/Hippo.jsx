import React, { Component } from 'react';
import PropTypes from 'prop-types';


export default class Hippo extends Component {

  static propTypes = {
    name: PropTypes.string.isRequired,
    score: PropTypes.number
  };

  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="hippo">
        <div className="hippo-name">
          { this.props.name }
        </div>
        <div className="hippo-score">
          { this.props.score }
        </div>
      </div>
    );
  }

}
