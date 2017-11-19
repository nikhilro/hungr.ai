import React, { Component } from 'react';
import Banner from './Banner'
import Players from './Players'
import Game from './Game'

export default class App extends Component {
  render() {
    return (
      <div className="app">
        <Banner />
        <div className="game-wrapper">
          <Players />
          <Game />
        </div>
      </div>
    );
  }
}
