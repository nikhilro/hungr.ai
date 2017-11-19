import React, { Component } from 'react';
import Start from './Start';
import Lobby from './Lobby';
import App from './App';

export default class Main extends Component {
  constructor(props) {
    super(props);

    this.state = {
      started: false,
      userJoined: false
    };

    this.onGetStarted = this.onGetStarted.bind(this);
    this.onJoinRoom = this.onJoinRoom.bind(this);
  }

  onGetStarted() {
    this.setState({ started: true });
  }

  onJoinRoom() {
    this.setState({ userJoined: true });
  }

  render() {
    let comp;
    if (!this.state.started && !this.state.userJoined) {
      comp = <Start
                onGetStarted={this.onGetStarted}
              />;
    } else comp = <App />
    return (
      <div class="header" id="header">
        { comp }
    	</div>
    );
  }
}
