import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import AppBar from 'material-ui/AppBar'
import Home from './Home'
import Sidebar from './Sidebar'
import Content from './Content'

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = { isLoggedIn: false };
  }

  onJoinRoom() {
    this.setState({ isLoggedIn: true });
    console.log('this.state.isLoggedIn', this.state.isLoggedIn);
  }

  render() {
    var body = (this.state.isLoggedIn) ? (
      <div>
        <AppBar
          title="Hungr.AI"
          style={{
            position: 'absolute',
            top: '0',
            left: '0',
            width: '100%',
          }}
          />
        <div className="content-wrapper">
          <Sidebar />
          <Content />
        </div>
      </div>) : <Home onJoinRoom={() => this.onJoinRoom()} />;
    return (
      <div>
        <MuiThemeProvider>
          { body }
        </MuiThemeProvider>
      </div>
    );
  }
}
