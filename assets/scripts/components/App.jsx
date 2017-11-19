import React, { Component } from 'react';
import Banner from './Banner'
import Players from './Players'
import Game from './Game'

export default class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      'players': [
        {
          'name': "Hungry Hippo",
          'colour': 'orange',
          'score': 0
        },
        {
          'name': "Veggie Potamus",
          'colour': 'green',
          'score': 0
        },
        {
          'name': "Bottomless Potamus",
          'colour': 'yellow',
          'score': 0
        },
        {
          'name': "Sweetie Potamus",
          'colour': 'blue',
          'score': 0
        }
      ]
    }
  };

  render() {
    return (
      <div className="app">
        <Banner />
        <div className="game-wrapper">
          <Players
            players={this.state.players}
            ballCount={0}
            total={16}
            />
          <Game />
        </div>
      </div>
    );
  }
}
