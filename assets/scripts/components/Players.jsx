import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Hippo from './Hippo';


export default class Players extends Component {

  static propTypes = {
    players: PropTypes.array,
    ballCount: PropTypes.number,
    total: PropTypes.number
  };

  constructor(props) {
    super(props);

    setPlayers(props.players, playerList => {
      this.state = {
        players: playerList,
        ballCount: 0,
        total: 0
      }
    });
  }

  setPlayers(players, callback) {
    callback(players.map(player => {
              return (
                <li>
                  <Hippo
                      name={player.name}
                      score={player.score}
                    />
                </li>
              );
            }));
  }

  componentWillReceiveProps(nextProps) {
    setPlayers(nextProps.players, playerList => {
      this.setState({
        players: playerList,
        ballCount: nextProps.ballCount
      });
    });
  }

  render() {
    return (
      <nav className="players">
           <div class="sidebar-header">
               <h3>Leaderboards</h3>
           </div>

           <ul class="list-unstyled components">
               { this.state.players }
           </ul>
       </nav>
    );
  }

}
