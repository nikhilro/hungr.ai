import React, { Component } from 'react';
import PropTypes from 'prop-types';

export default class Start extends Component {
  static propTypes = {
    onGetStarted: PropTypes.func
  };

  constructor(props) {
    super(props);
  }

  render() {
    return (
  		<div className="container">
  			<figure className="logo animated fadeInDown delay-07s">
  				<a href="#"><img src="img/logo.png" alt="" /></a>
  			</figure>
  			<h1 className="animated fadeInDown delay-07s">Welcome To HungrAI HungrAI Hippos</h1>
  			<ul className="we-create animated fadeInUp delay-1s">
  				<li>We are injecting articial intelligence into everyone's favourite game.</li>
  			</ul>
  			<a
          className="link animated fadeInUp delay-1s servicelink"
          onClick={this.props.onGetStarted}
        >Get Started</a>
  		</div>
    );
  }
}
